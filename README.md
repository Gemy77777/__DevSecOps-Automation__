# 🛡️ CyberSecurity Portfolio & Labs

Welcome to my cybersecurity repository! This repository serves as a centralized portfolio showcasing my practical experience, automated security scripts, and hands-on labs in network defense, system hardening, and security auditing.

---

## 🚀 Featured Projects

### 1. 🖥️ System Vulnerability Audit & Hardening
An automated security audit and hardening workflow executed on a primary host system to transition it from a vulnerable state into a proactive defense baseline.
* **Objective:** Audit the local system for misconfigurations, patch decay, and weak perimeter controls based on industry-standard security frameworks.
* **Key Components Checked:**
  * **Identity Front Door:** Evaluating local password complexity policies and multi-factor authentication (MFA) alignment with **NIST 800-63B standards**.
  * **Software Decay & Patch Management:** Tracking operating system hotfixes, active antivirus definitions, and monitoring for Shadow IT.
  * **Human Perimeter:** Auditing lingering administrative privileges (Privilege Creep) and securing local user controls by auditing and disabling deprecated Guest Accounts.
  * **Network & Endpoint Hygiene:** Ensuring proper inbound traffic controls via active OS Firewall profiles and full disk encryption (BitLocker/FileVault) for data-at-rest protection.
* **Implementation:** Built an automation script using **Python** (`subprocess`, `json`, `platform` modules) to interface with Windows PowerShell, fetch security baselines via CLI, and output structural audit reports.

---

## 🛠️ Tech Stack & Core Tools
* **Programming Languages:** Python (Automation, Scripting, Text Processing, Regular Expressions)
* **Scripting & Shells:** Windows PowerShell, Command Line Interface (CLI)
* **Security Frameworks:** NIST 800-63B Standards, CVSS v3.1 Scoring System
* **Environments:** Windows Server, Windows 10/11, Networking Lab Environments

---

## 📂 Repository Structure

```text
├── 01-System-Vulnerability-Audit/
│   ├── system_audit.py          # Python automation script for security auditing
│   ├── vulnerability_report.md  # 1-page professional vulnerability report
│   └── README.md                # Detailed project documentation
│
└── FUTURE-LABS/                 # Placeholders for upcoming security projects
