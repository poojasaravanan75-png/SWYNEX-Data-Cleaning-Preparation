# SWYNEX-Data-Cleaning-Preparation

Task 1 of my SWYNEX Technologies internship: cleaning and preparing a raw public dataset for analysis using Python (pandas).

## Dataset
- **Name:** Titanic passenger dataset
- **Source:** https://github.com/datasciencedojo/datasets (titanic.csv)
- **Size (raw):** 891 rows x 12 columns

## Issues Found
| Issue | Columns affected | Count |
|---|---|---|
| Missing values | Age | 177 |
| Missing values | Cabin | 687 |
| Missing values | Embarked | 2 |
| Duplicate records | all columns | 0 |
| Inconsistent values | Name (extra spaces), Embarked (S/C/Q short codes) | 2 names, 889 codes |
| Incorrect data types | Survived (0/1 number used as a Yes/No label), Pclass (category stored as number) | 2 columns |

## Cleaning Steps
1. Checked for duplicate rows (none found; the step is still in the script).
2. Removed extra spaces from `Name`, standardised `Sex` text case.
3. Replaced `Embarked` codes with full port names (S = Southampton, C = Cherbourg, Q = Queenstown).
4. Filled missing `Age` with the median (28), missing `Embarked` with the most common port, and missing `Cabin` with "Unknown".
5. Converted `Survived` from 0/1 to No/Yes, `Pclass` to a category, and `Age` to whole numbers.

## Result
- **Size (cleaned):** 891 rows x 12 columns
- Missing values after cleaning: 0
- Duplicate rows after cleaning: 0

## Files
- `raw_data.csv`: original dataset
- `clean_data.py`: cleaning script
- `cleaned_data.csv`: cleaned output

## How to Run
```bash
pip install pandas
python clean_data.py
```

## Tools
Python, pandas

## Key Learnings
- Always inspect missing values, duplicates and data types before cleaning.
- Choosing a fill method (median, most common value, "Unknown") depends on the column.
- Numbers that are really labels (like Survived, Pclass) should be treated as categories.
