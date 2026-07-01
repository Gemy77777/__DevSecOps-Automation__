# 🛡️ Security-DevOps Portfolio & Automation Labs

Welcome to my repository! This space serves as my personal portfolio, showcasing hands-on applications, security scripts, and defense automation tools built completely using **Python**.

The projects included here focus on proactive defense, cryptographic logic, identity security, risk assessment, and **security automation for DevOps workflows**.

---

## 🚀 Featured Projects

### 1. 🔍 Vulnerability Scanner
An automated system security scanner designed to audit local environments for critical gaps, misconfigurations, and software decay.

- **Core Focus:** Enforcing system hardening by checking local firewall profiles, monitoring patch management, identifying deprecated/high-risk accounts, and validating full-disk encryption baselines.
- **Implementation:** Built using Python's system integration modules to fetch active configurations via CLI tools and analyze system integrity.
- **Tech Stack:** Python, Subprocess, PowerShell Integration, Windows CLI

### 2. 🔐 Encryption Decryption System
A cryptographic tool designed to implement core defensive logic through text encryption and decryption algorithms.

- **Core Focus:** Understanding data protection at rest and in transit, data verification, and secure character shifting mechanisms.
- **Implementation:** Developed using Python to handle string manipulations, defensive logic, and basic mathematical operations for cryptographic security.
- **Tech Stack:** Python, String Manipulation, Cryptographic Logic

### 3. 🔑 Password Strength Checker
An identity security utility built to analyze and enforce credential safety boundaries.

- **Core Focus:** Aligning authentication benchmarks with modern industry frameworks (such as NIST standards) by checking length, character entropy, and complexity rules.
- **Implementation:** Python-based verification script that processes user credentials against algorithmic rule-sets to evaluate defensive readiness.
- **Tech Stack:** Python, NIST 800-63B Standards, Identity Security

### 4. 📧 Email Phishing Awareness
An educational security script focused on detecting social engineering indicators and raising human perimeter defenses.

- **Core Focus:** Analyzing communication headers, phishing indicators, and training defensive intuition against cloned or deceptive digital vectors.
- **Implementation:** Formatted in Python (`Phishing_Awarness.py`) to parse and flag common indicators used in credential harvesting and social engineering campaigns.
- **Tech Stack:** Python, Header Parsing, Social Engineering Detection

### 5. 📊 Log Analysis & Security Monitoring Tool ⭐ NEW
A Python-based automation tool for security log analysis and incident response.

- **Core Focus:** Automating the extraction and classification of IP addresses from system logs, filtering critical security events, and generating structured reports for security monitoring.
- **Key Features:**
  - Extracts and validates IPv4 addresses from log files using regex
  - Classifies IPs by risk: Safe (Private/Loopback), Warning (>30 occurrences), HIGH RISK (>100)
  - Filters critical events (error, fatal, failed, warning, exception)
  - Creates automatic backup archives of security-relevant logs
  - Generates JSON reports for SIEM integration and compliance auditing
- **Implementation:** Object-Oriented Python with modular design (LogFilter, IPExtractor, IPAnalyzer, Report classes)
- **Tech Stack:** Python, Regex, ipaddress Library, JSON, OOP, File I/O
- **Future Enhancements:** Docker containerization, CSV export, CI/CD integration

---

## 🛠️ Tech Stack & Skills

### Languages
- **Python** (Automation, Data Verification, String Parsing, Scripting, OOP)
- **C, C++** (Foundational Knowledge)

### Operating Systems & Infrastructure
- **Linux (RHEL, Kali)** - System Administration, User Management, Network Configuration
- **Windows Server** - RDP Administration, Firewall Management, PowerShell
- **Virtualization** - VMware, VirtualBox

### DevOps & Automation Tools
- **CI/CD:** Jenkins, GitHub Actions (Learning)
- **Containers:** Docker, Kubernetes (Learning)
- **Infrastructure as Code:** Terraform (Learning)
- **Version Control:** Git, GitHub

### Networking & Security
- **Protocols:** TCP/IP, DNS, HTTP/HTTPS, FTP, SMTP/POP3/IMAP
- **Security Tools:** Nmap, Burp Suite, Wireshark
- **Concepts:** Network Hygiene, Cryptographic Logic, Identity Verification, Firewall Hardening, DoS Mitigation

---

## 📌 Future Roadmap

- [ ] Add Docker containerization for all tools
- [ ] Integrate with GitHub Actions for automated security scanning
- [ ] Build a unified dashboard for all security tools
- [ ] Develop REST APIs for tool integration
- [ ] Create comprehensive test suites

---


> *"Security is not a product, but a process." - Bruce Schneier*

