from flask import Flask, request, jsonify
from utils import load_patterns, detect_sqli, log_attack

app = Flask(__name__)
patterns = load_patterns()  # Load once when server starts

@app.route('/')
def home():
    return "🔒 Welcome to the SQL Injection Detection API"

@app.route('/scan', methods=['GET', 'POST'])
def scan():
    # Accept payload via URL param (?input=...) or POST body
    user_input = request.args.get('input') or request.form.get('input') or ''
    
    matched_pattern = detect_sqli(user_input, patterns)
    
    if matched_pattern:
        # Log the attack details
        ip = request.remote_addr
        path = request.path
        log_attack(ip, path, user_input, matched_pattern)
        
        return jsonify({
            "input": user_input,
            "status": "SQL Injection Detected",
            "pattern_matched": matched_pattern
        }), 403  # Forbidden
    
    return jsonify({
        "input": user_input,
        "status": "Clean"
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
