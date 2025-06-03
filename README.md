# AUTOMATED-REPORT-GENERATION
COMPANY:CODTECH IT SOLUTIONS

Name :Trivedi Parth Yogeshbhai

Intern ID :CT04DN939

Domain:Python Programming

Duration:4 Weeks

Mentor:Neela Santhosh Kumar

📊 Sales Summary Report Generator
This project is a Python-based tool that reads employee sales data from a CSV file and generates a well-formatted PDF report summarizing the performance of various departments. It provides insights into the total and average sales, departmental breakdowns, and highlights the top-performing department.

🚀 Features
Reads and processes structured sales data from a CSV file

Generates a professional PDF report with:

Overall summary (total employees, total sales, average sales)

Department-wise breakdown (employee count, total sales)

Highlight of the top-performing department

Auto-handling of malformed or missing data entries

Clean and readable layout with alternating row colors for clarity

🧰 Technologies Used
Python 3.x

FPDF — for PDF generation

csv, collections, and datetime — for data handling and processing

📁 Project Structure
graphql
Copy
Edit
sales_report_generator/
├── sales_report.py        # Main script to generate the report
├── data.csv               # Input file containing sales data
├── sales_report_clean.pdf # Output PDF report (auto-generated)
└── README.md              # Project documentation
📝 CSV Format
The input data.csv file must contain the following headers:

python-repl
Copy
Edit
Name, Department, Sales
John Doe, Electronics, 15000
Jane Smith, Furniture, 18000
...
Name – Name of the employee

Department – Department name (string)

Sales – Total sales amount (integer)

▶️ How to Run
Install Dependencies

bash
Copy
Edit
pip install fpdf
Prepare your CSV file (e.g., data.csv) in the required format.

Run the script

bash
Copy
Edit
python sales_report.py
Output

A file named sales_report_clean.pdf will be generated in the same directory.

✅ Example Output
The PDF includes:

A header with the report title

Footer with generation timestamp

Overview with totals and averages

Department-wise summary in a tabular format

📌 Notes
The script automatically skips rows with invalid data (e.g., non-integer sales).

Modify csv_file and pdf_file variables in the script to customize input/output filenames.

