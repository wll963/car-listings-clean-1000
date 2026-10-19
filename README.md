# Car Listings Clean 1000

A cleaned tabular dataset of **1,000 used-vehicle listings** with 23 core attributes plus 3 derived Chinese category labels. The data covers listing snapshots from **2025-10-01 to 2026-08-21** and model years **2000–2026**.

一个包含 **1,000 条二手车挂牌记录** 的清洗后表格数据集，含 23 个原始字段和 3 个派生的中文分类字段。数据快照时间为 **2025-10-01 至 2026-08-21**，车辆年款为 **2000–2026**。

[![rows](https://img.shields.io/badge/rows-1%2C000-blue)](data/car_listings_clean_1000.csv)
[![columns](https://img.shields.io/badge/columns-23%20%2B%203-green)](schema.json)
[![duplicates](https://img.shields.io/badge/duplicate%20keys-0-brightgreen)](scripts/validate.py)

## Files

| File | Rows | Columns | Description |
|---|---:|---:|---|
| [`data/car_listings_clean_1000.csv`](data/car_listings_clean_1000.csv) | 1,000 | 23 | Cleaned core dataset (English values). |
| [`data/car_listings_clean_1000_classified.csv`](data/car_listings_clean_1000_classified.csv) | 1,000 | 26 | Core dataset + `vehicle_class`, `energy_class`, `category` (Chinese labels). |
| [`schema.json`](schema.json) | — | 26 | Field names, data types, descriptions, fill rates, cardinality. |
| [`stats.json`](stats.json) | — | — | Machine-readable summary statistics and distributions. |
| [`scripts/validate.py`](scripts/validate.py) | — | — | Reproducible integrity check (row count, unique keys, MD5). |

## Quick start

```python
import pandas as pd

url = "https://raw.githubusercontent.com/wll963/car-listings-clean-1000/main/data/car_listings_clean_1000.csv"
df = pd.read_csv(url)

print(df.shape)          # (1000, 23)
print(df["make"].value_counts().head())
```

Classified version:

```python
df = pd.read_csv(
    "https://raw.githubusercontent.com/wll963/car-listings-clean-1000/main/"
    "data/car_listings_clean_1000_classified.csv"
)
print(df[["bodyStyle", "vehicle_class", "fuelType", "energy_class", "category"]].head())
```

Validate a local copy:

```bash
python scripts/validate.py
```

## Schema

### Core fields (23)

| Column | Type | Fill | Description |
|---|---|---:|---|
| `_primaryKey` | string | 100% | Unique record ID (embedded VIN + dealer code + snapshot date). |
| `firstSeen` | date | 100% | Date the listing was first observed (`YYYY-MM-DD`). |
| `year` | int | 100% | Vehicle model year. |
| `make` | string | 100% | Manufacturer (40 distinct values). |
| `model` | string | 100% | Model name (255 distinct values). |
| `trim` | string | 100% | Trim level (235 distinct values). |
| `bodyStyle` | string | 100% | SUV, Sedan, Pickup, Wagon, Coupe, Hatchback, Minivan, Convertible, Van, Chassis. |
| `engine` | string | 100% | Engine configuration (e.g., `4 Cyl`, `6 Cyl`). |
| `displacement` | string | 100% | Engine displacement (e.g., `2.0 L`). |
| `drivetrain` | string | 100% | FWD, AWD, 4WD, RWD. |
| `transmission` | string | 100% | Automatic, Manual, Unspecified. |
| `fuelType` | string | 100% | Gasoline, Hybrid, Diesel, Electric, Flexible-Fuel, Alternative. |
| `mileage` | float | 100% | Odometer reading in miles. |
| `noAccidents` | bool | 71.2% | `True` when no accidents are reported; non-null values are all `True`, missing = not reported. |
| `serviceRecords` | bool | 95.6% | `True` when service history is available; non-null values are all `True`, missing = not reported. |
| `serviceRecordCount` | float | 100% | Number of service history records. |
| `personalUse` | bool | 73.0% | `True` when personal use is reported; non-null values are all `True`, missing = not reported. |
| `oneOwner` | bool | 55.6% | `True` when a single owner is reported; non-null values are all `True`, missing = not reported. |
| `onePrice` | float | 100% | CARFAX One Price estimate / asking price in USD. |
| `badge` | string | 68.0% | CARFAX value badge: `GOOD`, `GREAT`, `FAIR`. |
| `snapshotDamageSeverity` | string | 6.0% | Damage severity from the listing snapshot. |
| `reliabilityBadge` | string | 26.8% | Reliability badge (e.g., `GOOD`, `AVERAGE`). |
| `reliabilityAvgCost` | float | 26.8% | Average repair cost in USD. |

### Derived Chinese labels (3, classified file only)

| Column | Fill | Description |
|---|---:|---|
| `vehicle_class` | 100% | Body-style class derived from `bodyStyle`: 小轿车 (194), SUV (210), 皮卡 (165), 旅行车 (114), 轿跑 (103), 两厢车 (90), MPV (71), 敞篷车 (32), 厢式车 (20), 底盘车 (1). |
| `energy_class` | 100% | Energy-source class derived from `fuelType`: 燃油 (794), 混动 (87), 柴油 (66), 纯电 (32), 灵活燃料 (20), 其他能源 (1). |
| `category` | 100% | Combined label, `energy_class` + `vehicle_class`, e.g. `燃油SUV` (178), `燃油小轿车` (147), `燃油旅行车` (113). |

## Key statistics

| Metric | Value |
|---|---|
| Rows | 1,000 |
| Core columns | 23 |
| Classified columns | 26 |
| Duplicate `_primaryKey` | 0 |
| Distinct makes | 40 |
| Distinct models | 255 |
| Model-year range | 2000–2026 |
| Mileage range | 12–312,618 miles |
| `onePrice` range | $1,380–$343,280 |
| Snapshot period | 2025-10-01 – 2026-08-21 |

**Top makes:** Ford 110, Toyota 96, Subaru 91, Chevrolet 90, Honda 88, BMW 62, GMC 51, Kia 37, Mercedes-Benz 34, Jeep 33.

**Body styles:** SUV 210, Sedan 194, Pickup 165, Wagon 114, Coupe 103, Hatchback 90, Minivan 71, Convertible 32, Van 20, Chassis 1.

**Fuel types:** Gasoline 794, Hybrid 87, Diesel 66, Electric 32, Flexible-Fuel 20, Alternative 1.

**Drivetrains:** FWD 310, AWD 293, 4WD 230, RWD 167.

## Data notes

- **Missing booleans are not `False`.** In this cleaned export, the boolean columns only contain `True` when present; `NaN` means the attribute was not reported. Treat missing and false separately in modeling.
- **`noAccidents`, `personalUse`, `oneOwner`, and `serviceRecords` are constant when present.** They are useful as availability indicators rather than as class-balanced features.
- **The `_primaryKey` embeds a VIN-derived string** (`VIN + dealer code + snapshot date`). No dealer names, phone numbers, addresses, or listing URLs are included in this release. Hash `_primaryKey` if you need an anonymous join key.
- **Prices are USD; mileage is in miles.** No normalization or currency conversion has been applied.
- **Snapshot data, not transaction data.** `onePrice` is the listed / CARFAX One Price estimate, not a final sale price.
- **Classified file is derived**, not independently labeled: `vehicle_class` and `energy_class` are rule-based mappings of `bodyStyle` and `fuelType`, and `category` is their concatenation.

## Source, license, and intended use

The records are derived from CARFAX vehicle-listing snapshots. This repository does not grant a license to the underlying source data; any reuse must comply with CARFAX's terms and applicable law. The cleaned tabular compilation is shared for research and educational use. No license (open or otherwise) is asserted over the source records. If you are the rights holder and want the repository changed or removed, please open an issue.

This dataset is **not** intended for pricing, lending, insurance, or any high-stakes decision about individuals or dealers. It has not been audited for demographic or geographic representativeness.

## Citation

```bibtex
@misc{car_listings_clean_1000,
  title  = {Car Listings Clean 1000},
  year   = {2026},
  note   = {1,000 cleaned used-vehicle listings, 23 core attributes + 3 derived categories},
  url    = {https://github.com/wll963/car-listings-clean-1000}
}
```

## Version

- **v1.0.0** — Initial release: 1,000 rows, 23 core fields, 26 classified fields. MD5 of the cleaned CSV: `ff049f82c7e193452904ffa3fe1ac8c8`; classified CSV: `e59f826a9a7e07972f3f46518f5a0335`.

---

### 中文说明

- **数据规模**：1,000 条二手车挂牌记录，无重复主键；核心字段 23 个，分类版 26 个。
- **字段含义**：`schema.json` 提供逐字段类型、缺失率和取值说明；`stats.json` 提供可机读的分布统计。
- **缺失值语义**：布尔字段为空表示“未报告”，不等于 `False`；建模时请将缺失与否定区分开。
- **中文标签**：`vehicle_class`（车型）、`energy_class`（能源类型）由原始字段规则映射得到，`category` 为二者组合。
- **隐私**：本版本不含经销商名称、电话、地址和挂牌链接；`_primaryKey` 内含 VIN 派生串，如需匿名化请先哈希。
- **来源与许可**：数据源自 CARFAX 挂牌快照，仓库不授予底层数据的许可；使用需遵守 CARFAX 条款及适用法律，仅供研究与教学使用。
