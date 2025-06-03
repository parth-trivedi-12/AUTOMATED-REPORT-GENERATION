import csv
from fpdf import FPDF
from collections import defaultdict
from datetime import datetime

class PDFReport(FPDF):
    def header(self):
        self.set_fill_color(0, 102, 204)
        self.rect(0, 0, 210, 20, 'F')
        self.set_text_color(255, 255, 255)
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Sales Summary Report", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 9)
        self.set_text_color(100)
        self.cell(0, 10, f"Generated on {datetime.now().strftime('%d-%m-%Y %H:%M')}", align="C")

def read_data(file_path):
    data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                name = row['Name'].strip()
                dept = row['Department'].strip()
                sales = int(row['Sales'])
                data.append({'Name': name, 'Department': dept, 'Sales': sales})
            except (ValueError, KeyError):
                continue
    return data

def analyze_data(data):
    summary = defaultdict(lambda: {'Count': 0, 'TotalSales': 0})
    total_sales = 0

    for entry in data:
        dept = entry['Department']
        summary[dept]['Count'] += 1
        summary[dept]['TotalSales'] += entry['Sales']
        total_sales += entry['Sales']

    total_employees = sum(v['Count'] for v in summary.values())
    avg_sales = total_sales / total_employees if total_employees else 0
    top_dept = max(summary.items(), key=lambda x: x[1]['TotalSales'])[0] if summary else 'N/A'

    return summary, total_sales, avg_sales, top_dept, total_employees

def generate_pdf(summary, total_sales, avg_sales, top_dept, total_employees, output_file):
    pdf = PDFReport()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.set_text_color(0)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Overview", ln=True)
    pdf.set_font("Arial", "", 11)
    pdf.ln(2)
    pdf.cell(0, 8, f"Total Employees: {total_employees}", ln=True)
    pdf.cell(0, 8, f"Total Sales: Rs. {total_sales}", ln=True)
    pdf.cell(0, 8, f"Average Sales per Employee: Rs. {avg_sales:.2f}", ln=True)
    pdf.cell(0, 8, f"Top Performing Department: {top_dept}", ln=True)
    pdf.ln(5)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Department-wise Summary", ln=True)
    pdf.ln(2)

    # Table Headers
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(60, 10, "Department", border=1, fill=True)
    pdf.cell(40, 10, "Employees", border=1, fill=True)
    pdf.cell(60, 10, "Total Sales (Rs.)", border=1, fill=True)
    pdf.ln()

    # Table Rows
    pdf.set_font("Arial", "", 11)
    fill = False
    for dept, info in summary.items():
        pdf.set_fill_color(245, 245, 245) if fill else pdf.set_fill_color(255)
        pdf.cell(60, 10, dept, border=1, fill=fill)
        pdf.cell(40, 10, str(info['Count']), border=1, fill=fill)
        pdf.cell(60, 10, str(info['TotalSales']), border=1, fill=fill)
        pdf.ln()
        fill = not fill

    pdf.output(output_file)
    print(f"✅ Report generated: {output_file}")

if __name__ == "__main__":
    csv_file = "data.csv"
    pdf_file = "sales_report_clean.pdf"
    data = read_data(csv_file)
    summary, total_sales, avg_sales, top_dept, total_employees = analyze_data(data)
    generate_pdf(summary, total_sales, avg_sales, top_dept, total_employees, pdf_file)

