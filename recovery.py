solutions = {
    "ransomware": [
        "Disconnect device from internet immediately.",
        "Do NOT pay ransom.",
        "Boot into Safe Mode.",
        "Run full antivirus scan.",
        "Check NoMoreRansom.org for decryptor tools."
    ],

    "phishing": [
        "Do not click suspicious links.",
        "Change passwords immediately.",
        "Enable Two-Factor Authentication.",
        "Contact your bank if financial data was shared."
    ],

    "malware": [
        "Disconnect from internet.",
        "Uninstall suspicious programs.",
        "Run antivirus scan.",
        "Clear browser cache."
    ],

    "account_breach": [
        "Reset your password immediately.",
        "Enable 2FA.",
        "Check account activity.",
        "Log out from all sessions."
    ],

    "unknown": [
        "Run a full antivirus scan.",
        "Avoid clicking unknown links.",
        "Consult a cybersecurity professional."
    ]
}


def get_recovery_steps(threat_type):
    return solutions.get(threat_type, solutions["unknown"])
