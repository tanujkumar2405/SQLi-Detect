import os
from fpdf import FPDF
from datetime import datetime
  
LOG_FILE = os.path.join("logs", "sqli_logs.txt")
REPORTS_DIR = "reports"

class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "SQL Injection Detection Report", 0, 1, "C")
        self.ln(5)
    
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        page_num = f"Page {self.page_no()}"
        self.cell(0, 10, page_num, 0, 0, "C")

def parse_log_line(line):
    # Example log line:
    # [2025-07-17 14:20:15] IP: 192.168.1.100 | Endpoint: /batch-test | Payload: 1 OR 1=1 | Pattern: (?!)(\bOR\b|\bAND\b)\s\d+=\d+
    parts = line.strip().split("|")
    if len(parts) < 4:
        return None
    
    try:
        timestamp = line.split("]")[0].strip("[")
        ip = parts[0].split("IP:")[1].strip()
        endpoint = parts[1].split("Endpoint:")[1].strip()
        payload = parts[2].split("Payload:")[1].strip()
        pattern = parts[3].split("Pattern:")[1].strip()
        return {
            "timestamp": timestamp,
            "ip": ip,
            "endpoint": endpoint,
            "payload": payload,
            "pattern": pattern
        }
    except IndexError:
        return None

def generate_report():
    print("No logd Found to generate report.")
    return

    os.makedirs(REPORTS_DIR, exist_ok=True)
    pdf = PDFReport()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    with open(LOG_FILE, "r") as file:
        lines = file.readlines()
    
    if not lines:
        print("Log file is empty. No report generated.")
        return
    
    for line in lines:
        entry = parse_log_line(line)
        if entry:
            pdf.set_font("Arial", "B", 11)
            pdf.cell(0, 10, f"Timestamp: {entry['timestamp']}", ln=1)
            pdf.set_font("Arial", size=11)
            pdf.cell(0, 8, f"IP: {entry['ip']} | Endpoint: {entry['endpoint']}", ln=1)
            pdf.multi_cell(0, 8, f"Payload: {entry['payload']}")
            pdf.multi_cell(0, 8, f"Matched Pattern: {entry['pattern']}")
            pdf.ln(5)
    
    report_filename = os.path.join(REPORTS_DIR, f"sqli_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf")
    pdf.output(report_filename)
    
    print(f"Report generated: {report_filename}")

if __name__ == "__main__":
    generate_report()
