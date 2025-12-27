#!/bin/bash
# =========================================
# AEGIS-RED-RECON
# Ethical Reconnaissance Tool (LAB USE ONLY)
# Author:Anubhav Tyagi
# =========================================

if [ -z "$1" ]; then
  echo "Usage: aegis_red_recon.sh <target-ip>"
  echo "Example: aegis_red_recon.sh 127.0.0.1"
  exit 1
fi

TARGET="$1"
OUT="reports/recon_${TARGET}_$(date +%F_%H-%M).txt"

echo "======================================" | tee "$OUT"
echo " AEGIS RED TEAM RECONNAISSANCE REPORT" | tee -a "$OUT"
echo " Target: $TARGET" | tee -a "$OUT"
echo " Date: $(date)" | tee -a "$OUT"
echo " NOTE: AUTHORIZED / LAB USE ONLY" | tee -a "$OUT"
echo "======================================" | tee -a "$OUT"
echo | tee -a "$OUT"

echo "[+] Host Reachability Check" | tee -a "$OUT"
ping -c 2 "$TARGET" &>/dev/null && echo "Host is reachable" | tee -a "$OUT"
echo | tee -a "$OUT"

echo "[+] Top Port Scan (Safe)" | tee -a "$OUT"
nmap -Pn -T3 --top-ports 100 "$TARGET" | tee -a "$OUT"
echo | tee -a "$OUT"

echo "[+] Service Enumeration" | tee -a "$OUT"
nmap -Pn -sV --top-ports 20 "$TARGET" | tee -a "$OUT"
echo | tee -a "$OUT"

echo "[+] Web Exposure Check" | tee -a "$OUT"
nmap -Pn -p 80,443 "$TARGET" | tee -a "$OUT"

echo | tee -a "$OUT"
echo "[✔] Reconnaissance Complete" | tee -a "$OUT"
echo "[✔] Report saved to $OUT"
