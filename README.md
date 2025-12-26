# Syntecxhub_SQL_Injection_Scanner
A Python-based SQL Injection vulnerability scanner developed as part of the Syntecxhub Internship program for educational and ethical security testing.
# SQL Injection Vulnerability Scanner (Python)
 
This project is created strictly for **educational and ethical security testing purposes**.


## ⚠️ Disclaimer

This tool is intended **only for learning and authorized security testing**.

❌ Do NOT use this tool on websites or systems without proper permission.  
The author and Syntecxhub are **not responsible for any misuse** of this software.

---

## 🚀 Features

- Detects **Error-based SQL Injection**
- Detects **Boolean-based SQL Injection**
- Detects **Time-based (Blind) SQL Injection**
- Baseline response comparison to reduce false positives
- GET-based parameter scanning
- Scan results saved to a log file

---

🛠️ Requirements
- Python 3.8 or higher
- `requests` library

Install dependencies using:

pip install -r requirements.txt

📂 Project Structure
Syntecxhub_SQL_Injection_Scanner/
│
├── sql_injection_scanner.py
├── sql_payloads.txt
├── sql_scan_results.log
├── requirements.txt
└── README.md

▶️ Usage
Add SQL injection payloads in sql_payloads.txt

Configure the target URL and parameter in sql_injection_scanner.py

Run the scanner:

python sql_injection_scanner.py
View results in the terminal and in sql_scan_results.log

🧪 Tested On (Legal & Authorized Targets)
http://testphp.vulnweb.com

DVWA (Local setup)

bWAPP (Local setup)

📌 Sample Output

[!] Vulnerable (SQL error detected) with payload: 1'
[!] Vulnerable (Response length differs) with payload: 1 OR 1=1
[!] Vulnerable (Time delay detected) with payload: 1 AND SLEEP(5)
[-] Not vulnerable with payload: 1 AND 1=2

🔮 Future Enhancements
POST parameter scanning

Automatic parameter discovery

Multi-threaded scanning

Web Application Firewall (WAF) detection

HTML report generation
