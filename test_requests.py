import requests

URL = "http://localhost:5000/test"

# List of test inputs: safe and malicious
test_inputs = [
    "normalinput",
    "' OR '1'='1",
    "'; DROP TABLE users;--",
    "admin' --",
    "1 OR 1=1",
    "test@example.com",
    "password123",
    "UNION SELECT NULL, NULL, NULL",
    "1' AND 1=1 --",
    "Robert'); DROP TABLE Students;--"
]

def run_tests():
    print(f"Sending {len(test_inputs)} test inputs to {URL}...\n")
    for i, payload in enumerate(test_inputs, 1):
        try:
            res = requests.get(URL, params={"input": payload})
            print(f"[{i}] Sent: {payload}\nResponse: {res.text}\n")
        except requests.exceptions.RequestException as e:
            print(f"[{i}] Failed to send: {payload}\nError: {e}\n")

if __name__ == "__main__":
    run_tests()
