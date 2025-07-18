# SQLi-Detect

![SQLi-Detect](https://img.shields.io/badge/SQLi-Detect-blue?style=for-the-badge&logo=python)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)
  
---

## 🔒 What is SQLi-Detect?

**SQLi-Detect** is a powerful, yet lightweight SQL Injection Detection tool built in Python. It helps security professionals, developers, and students detect and log suspicious inputs that may indicate SQL injection attempts.
 
Using carefully crafted regex patterns, this tool can:

- Identify common and advanced SQLi payloads
- Log attack details with timestamps, IP addresses, and affected endpoints
- Provide a simple command-line interface for on-the-fly testing
- Serve as a REST API for integration into web applications and automated pipelines
- Generate detailed PDF reports summarizing detected attacks for auditing and compliance

SQL injection remains one of the most critical web security vulnerabilities. **SQLi-Detect** empowers you to stay ahead by detecting these attacks early and effectively.

---

## 🚀 Features

| Feature                      | Description                                      |
|-----------------------------|------------------------------------------------|
| Regex-based SQLi detection   | Detects classic and complex SQL injection payloads via regex. |
| Real-time logging            | Logs attack metadata including IP, endpoint, payload, and timestamp. |
| CLI interactive mode         | Quickly test inputs from your terminal.        |
| Flask REST API               | Integrate SQLi detection into your apps easily.|
| PDF report generation        | Create professional reports from logs.         |
| Automated testing scripts    | Validate detection with predefined payloads.   |
| Modular & extensible         | Easily add or customize detection patterns and reporting formats. |

---

## 📚 Why SQLi-Detect?

SQL Injection attacks exploit vulnerabilities in poorly sanitized inputs to execute malicious SQL commands. They can lead to unauthorized data access, data corruption, or even full system compromise.

**SQLi-Detect** provides a practical, educational, and extendable platform for:

- **Developers:** Quickly scan and secure inputs during development.
- **Security Analysts:** Monitor live traffic or logs to identify attacks.
- **Students:** Learn how SQLi detection works and build upon it.
- **Teams:** Use the API for automated security pipelines or CI/CD integration.

---

## 🛠️ Technology Stack

- **Python 3.6+** — Core language  
- **Flask** — Lightweight REST API server  
- **Regex** — Pattern matching for SQLi detection  
- **FPDF** — PDF report creation  
- **Colorama** — Colorful CLI output  
- **Requests** — Automated API testing  

---

## 📦 Installation

1. **Clone the repository:**

```bash
   git clone https://github.com/tanujkumar2405/SQLi-Detect.git
   cd SQLi-Detect
```

2. **Install dependencies:**

```bash
   pip install -r requirements.txt
```

3. **(Optional) Create folders if not present:**

```bash
   Copy code
   mkdir logs reports
```

---

## 🧑‍💻 Usage

1. **Run the Flask API:**

Start the detection API:

```bash
   python run.py
```
API Base URL: *http://127.0.0.1:5000/*

Test scan endpoint:
*GET /scan?input=<your_input_here>*

Example request:

```bash
   curl "http://127.0.0.1:5000/scan?input=' OR 1=1 --"
```
Example response:

```json
{
  "input": "' OR 1=1 --",
  "status": "SQL Injection Detected",
  "pattern_matched": "(?i)(\\bOR\\b|\\bAND\\b)\\s+\\d+=\\d+"
}
```

2. **Use the CLI Detection Tool:**

```bash
   python detector.py
```

- Enter any input to test for SQLi.
- Type *exit* to quit.
- Suspicious input triggers a warning and logs the attempt.

3. **Generate PDF Reports:**
Generate professional reports of logged SQLi attempts:

```bash
   python report_generator.py
```

- Reports are saved in the *reports/* directory.
- Each report includes timestamp, IP, endpoint, payload, and matched pattern.

4. **Automated Testing:**

Use the *test_requests.py* script to send multiple test payloads automatically to the API:

```bash
   python test_requests.py
```

---


## 🗂️ Project Structure

SQLi-Detect/
├── patterns.txt          # Regex patterns for SQL injection detection
├── utils.py              # Utility functions: load patterns, detect, log
├── detector.py           # CLI interactive SQLi detection tool
├── run.py                # Flask API for SQLi detection
├── report_generator.py   # Generate PDF reports from logs
├── test_requests.py      # Script for automated API payload tests
├── requirements.txt      # Python dependencies
├── logs/                 # Directory storing detection logs
└── reports/              # Directory storing generated PDF reports


---


## 🔧 How It Works (Brief Overview)

1. Patterns: Regex rules loaded from *patterns.txt* represent common SQL injection syntax *(e.g.,' OR 1=1 --)*.

2. Detection: Input payloads are scanned against these regex patterns.

3. Logging: When a match is found, details (IP, input, matched pattern) are logged with a timestamp.

4. Interfaces: Detection can be done via CLI or API.

5. Reporting: Logged entries can be converted into human-readable PDF reports.


---


## 🤝 Contributing

Contributions, improvements, and feature requests are welcome! Please:

   1. Fork the repository.

   2. Create a new branch for your feature or bugfix.

   3. Commit your changes with clear messages.

   4. Submit a pull request with details about your changes.


---


## 📂 Info Folder

All function-level and module-level explanations are available inside the [`info/`](./info) directory.


---


## 📜 License

This project is licensed under the [MIT License](LICENSE.txt).  
See the [LICENSE.txt](LICENSE.txt) file for details.


---


## 🙋‍♂️ Contact

Created by **Tanuj Kumar**

Email: tanujkumar2405@gmail.com

GitHub: https://github.com/tanujkumar2405


---


## ⚠️ Disclaimer

**SQLi-Detect** is designed for educational and ethical security purposes only. Use it responsibly on systems and data you own or have permission to test.


---


## 🌟 Stay Secure!

SQL Injection attacks can cause serious harm. By using tools like **SQLi-Detect**, you take a proactive step towards securing your applications and data. Happy securing! 🔐
