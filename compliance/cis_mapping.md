# aegis-SECOPS SUITE: CIS Benchmark Mapping

This document maps the checks performed by AEGIS-SECOPS-SUITE
to the **Center for Internet Security (CIS) Linux Benchmarks**.

| Check                                   | CIS Control Reference              | Notes |
|----------------------------------------|----------------------------------|-------|
| Password max days                        | CIS 5.1.2                        | Ensures passwords expire |
| Password min days                        | CIS 5.1.3                        | Prevents users from reusing old passwords immediately |
| Password warning age                     | CIS 5.1.4                        | Notifies users before password expiry |
| SSH root login                           | CIS 5.2.2                        | Root login via SSH should be disabled |
| SSH password authentication             | CIS 5.2.3                        | Enforces key-based authentication |
| PAM password complexity                  | CIS 5.1.7                        | Enforces strong passwords using PAM |
| Sudo users                               | CIS 5.3.1                        | Monitors users with administrative privileges |

## Usage
- Refer to this table when generating reports.  
- Helps SOC analysts and auditors understand which controls are covered.  

## Disclaimer
- This mapping is for **educational and lab use**.  
- Always consult official CIS benchmarks for production environments.
