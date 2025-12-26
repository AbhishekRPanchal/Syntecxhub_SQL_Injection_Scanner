import requests
import time

TARGET_URL = "http://testphp.vulnweb.com/artists.php"
PARAM = "artist"
LOG_FILE = "sql_scan_results.log"
PAYLOAD_FILE = "sql_payloads.txt"

print("Starting SQL Injection Scan...\n")

# --- BASELINE REQUEST ---
baseline_response = requests.get(TARGET_URL, params={PARAM: "1"})
baseline_text = baseline_response.text.lower()
baseline_length = len(baseline_text)

sql_errors = [
    "you have an error in your sql syntax",
    "mysql_fetch",
    "mysql_num_rows",
    "warning: mysql",
    "odbc sql",
    "unclosed quotation mark",
    "quoted string not properly terminated"
]

with open(PAYLOAD_FILE, "r") as f:
    payloads = [line.strip() for line in f if line.strip()]

with open(LOG_FILE, "w") as log:
    log.write("SQL Injection Scan Results\n\n")

    for payload in payloads:
        params = {PARAM: payload}

        start = time.time()
        response = requests.get(TARGET_URL, params=params)
        end = time.time()

        response_text = response.text.lower()
        response_length = len(response_text)
        time_diff = end - start

        vulnerable = False
        reason = ""

        # 1️⃣ Time-based SQLi
        if time_diff > 4:
            vulnerable = True
            reason = "Time delay detected"

        # 2️⃣ Error-based SQLi
        else:
            for err in sql_errors:
                if err in response_text and err not in baseline_text:
                    vulnerable = True
                    reason = "SQL error detected"
                    break

        # 3️⃣ Boolean-based SQLi
        if not vulnerable and abs(response_length - baseline_length) > 150:
            vulnerable = True
            reason = "Response length differs"

        if vulnerable:
            result = f"[!] Vulnerable ({reason}) with payload: {payload}"
        else:
            result = f"[-] Not vulnerable with payload: {payload}"

        print(result)
        log.write(result + "\n")

print("\n✅ Scan completed. Results saved in sql_scan_results.log")
