#!/bin/bash

while true; do
  clear
  echo "======================================="
  echo "        AEGIS SECOPS SUITE"
  echo "======================================="
  echo "1. Password & Access Policy Audit"
  echo "2. Security Risk Scoring"
  echo "3. Ethical Recon (LAB ONLY)"
  echo "4. View Reports"
  echo "5. Exit"
  echo "---------------------------------------"
  read -p "Select an option: " choice

  case $choice in
    1)
      sudo python3 core/aegis_passcheck.py
      read -p "Press Enter to continue..."
      ;;
    2)
      python3 core/risk_score.py
      read -p "Press Enter to continue..."
      ;;
    3)
      read -p "Enter Target IP (LAB ONLY): " target
      sudo offensive/aegis_red_recon.sh "$target"
      read -p "Press Enter to continue..."
      ;;
    4)
      ls -lh reports/
      read -p "Press Enter to continue..."
      ;;
    5)
      echo "Exiting AEGIS-SECOPS-SUITE"
      exit 0
      ;;
    *)
      echo "Invalid option"
      sleep 1
      ;;
  esac
done

