#!/usr/bin/env python3
# =========================================
# AEGIS-RISK-SCORE
# Calculates security risk score from passcheck report
# Author: Anubhav Tyagi
# =========================================

import json

# Load JSON report
with open("reports/passcheck.json") as f:
    data = json.load(f)

# Initialize score
score = 100
issues = []

# Rule 1: SSH root login enabled
if "yes" in data.get("ssh_root_login", "").lower():
    score -= 30
    issues.append("SSH root login enabled")

# Rule 2: Empty password accounts exist
if data.get("empty_password_accounts"):
    score -= 40
    issues.append("Empty password accounts detected")

# Rule 3: Sudo users exist
sudo_users = data.get("sudo_users", "")
if sudo_users and sudo_users.strip():
    score -= 10
    issues.append(f"Sudo users present: {sudo_users}")

# Rule 4: Weak PAM password policy
if not data.get("pam_password_policy"):
    score -= 20
    issues.append("No PAM password complexity configured")

# Display results
print("========== AEGIS RISK SCORE ==========")
print(f"Security Risk Score: {score}/100")
if score >= 80:
    print("Risk Level: LOW")
elif score >= 50:
    print("Risk Level: MODERATE")
else:
    print("Risk Level: HIGH")

if issues:
    print("\nDetected Issues:")
    for i in issues:
        print(f"- {i}")
print("======================================")
