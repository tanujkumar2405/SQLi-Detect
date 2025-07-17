import os
import re
from datetime import datetime

# Define the log file path (works on Windows/Linux/Mac)
LOG_FILE = os.path.join("logs", "sqli_logs.txt")

def load_patterns(file_path='patterns.txt'):
    """
    Load regex patterns from a file, ignoring empty lines.
    Returns a list of string patterns.
    """
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip()]

def detect_sqli(payload, patterns):
    """
    Check if the given input payload matches any SQLi pattern.
    Returns the matched pattern if found, else None.
    """
    for pattern in patterns:
        if re.search(pattern, payload):
            return pattern  # Return the first matched pattern
    return None

def log_attack(ip, endpoint, payload, pattern):
    """
    Append detected SQLi attack details with timestamp to the log file.
    """
    # Ensure logs directory exists
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = (f"[{timestamp}] IP: {ip} | Endpoint: {endpoint} | "
                 f"Payload: {payload} | Pattern: {pattern}\n")

    with open(LOG_FILE, "a") as log:
        log.write(log_entry)
