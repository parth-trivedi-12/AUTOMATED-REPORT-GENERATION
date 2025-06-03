# AUTOMATED-REPORT-GENERATION
COMPANY:CODTECH IT SOLUTIONS

Name :Trivedi Parth Yogeshbhai

Intern ID :CT04DN939

Domain:Python Programming

Duration:4 Weeks

Mentor:Neela Santhosh Kumar



# 📊 Sales Summary Report Generator

This Python project reads employee sales data from a CSV file and generates a clean, professional PDF report summarizing sales performance across departments.

## 🚀 Features

- Reads structured sales data from a `.csv` file
- Generates a professional PDF report with:
  - ✅ Total employees and sales
  - 📈 Average sales per employee
  - 🏆 Top-performing department
  - 🗂 Department-wise employee and sales summary
- Ignores malformed or missing data entries
- Alternating row colors for better readability

## 🛠 Technologies Used

- Python 3
- [FPDF](https://pyfpdf.github.io/fpdf2/) for PDF generation
- Built-in modules: `csv`, `collections`, `datetime`

## 📁 File Structure

```

📦 sales-summary-report/
├── sales\_report.py            # Main script
├── data.csv                   # Input CSV data file
├── sales\_report\_clean.pdf     # Generated PDF report
└── README.md                  # Project documentation

```

## 📝 CSV Format

The input CSV (`data.csv`) should include the following headers:

```

Name,Department,Sales
John Doe,Electronics,15000
Jane Smith,Furniture,18000
...

````

- `Name` — Employee name (string)
- `Department` — Department name (string)
- `Sales` — Sales amount (integer)

## ▶️ How to Use

1. **Install FPDF**

```bash
pip install fpdf
````

2. **Place your CSV file** (named `data.csv`) in the project directory.

3. **Run the script**

```bash
python sales_report.py
```

4. **View Output**

The script will generate `sales_report_clean.pdf` in the same directory.

## 📌 Notes

* Rows with missing or non-numeric sales values are skipped.
* You can rename `data.csv` or `sales_report_clean.pdf` in the script if needed.



