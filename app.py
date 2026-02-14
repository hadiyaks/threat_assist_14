from flask import Flask, render_template, request, jsonify
from classifier import classify_issue
from recovery import get_recovery_steps
from reporting import get_reporting_link

# 🔹 FIRST create Flask app
app = Flask(__name__)

# 🔹 Home route
@app.route("/")
def home():
    return render_template("index.html")

# 🔹 Analyze route
@app.route("/analyze", methods=["POST"])
def analyze():
    user_input = request.json["message"]
    country = request.json["country"]

    threat, confidence = classify_issue(user_input)
    steps = get_recovery_steps(threat)
    report = get_reporting_link(country)

    # Threat severity
    if threat == "ransomware":
        severity = "High"
    elif threat == "phishing":
        severity = "Medium"
    elif threat == "malware":
        severity = "Medium"
    elif threat == "account_breach":
        severity = "High"
    else:
        severity = "Low"

    response = {
        "threat": threat,
        "confidence": confidence,
        "severity": severity,
        "steps": steps,
        "report_name": report["name"],
        "report_url": report["url"]
    }

    return jsonify(response)


# 🔹 Run app
if __name__ == "__main__":
    app.run(host="0.0.0",port=1000)
