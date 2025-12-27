#!/usr/bin/env python3
# =========================================
# AEGIS-PASSCHECK
# Enterprise Password & Access Policy Analyzer
# Author:Anubhav Tyagi
# Ethical / Authorized use only
# =========================================

import subprocess
import json
import os
import datetime

def run(cmd):
    return subprocess.getoutput(cmd)

report = {
    "generated_on": str(datetime.datetime.now()),

    "password_policy": run(
        "grep -E 'PASS_MAX_DAYS|PASS_MIN_DAYS|PASS_WARN_AGE' /etc/login.defs"
    ),

    "uid_0_accounts": run(
        "awk -F: '$3==0 {print $1}' /etc/passwd"
    ),

    "empty_password_accounts": run(
        "awk -F: '($2==\"\"){print $1}' /etc/shadow 2>/dev/null"
    ),

    "ssh_root_login": run(
        "grep -i '^PermitRootLogin' /etc/ssh/sshd_config 2>/dev/null"
    ),

    "ssh_password_authentication": run(
        "grep -i '^PasswordAuthentication' /etc/ssh/sshd_config 2>/dev/null"
    ),

    "pam_password_policy": run(
        "grep pam_pwquality /etc/pam.d/common-password 2>/dev/null"
    ),

    "sudo_users": run(
        "getent group sudo | cut -d: -f4"
    )
}

# Ensure reports directory exists
os.makedirs("reports", exist_ok=True)

# Write JSON report
with open("reports/passcheck.json", "w") as f:
    json.dump(report, f, indent=4)

print("[✔] AEGIS-PASSCHECK completed successfully")
print("[✔] Report generated: reports/passcheck.json")
