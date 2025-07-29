
# 🛡️ VulneraScan – Automated Web & Network Vulnerability Scanner (CLI)

**VulneraScan** is a modular and lightweight command-line tool for scanning web applications and network systems for common vulnerabilities. It’s built for penetration testers, red teamers, and cybersecurity learners to perform fast and extensible scans in a controlled environment.

---

## 🚀 Features

- 🔍 **Network Scanning** using Nmap
- 🛡️ **Web Vulnerability Detection**
  - Missing security headers
  - Reflected XSS check
  - Directory listing exposure
  - Sensitive file detection
- 📁 **Directory Brute-force**
- 🔒 **SSL Certificate Inspection**
- 🧱 **CMS/Technology Fingerprinting**
- 📄 **.txt Report Generation**
- ⚙️ CLI-flag-based scan execution

---

## 📦 Requirements

Install dependencies inside a virtual environment:

```bash
pip install -r requirements.txt
```

Ensure `nmap` is installed on your system:

```bash
sudo apt install nmap
```

---

## ⚙️ Usage

```bash
python3 main.py --target http://example.com --network --web --dir --ssl --cms --output report.txt
```

### 🎛️ Scan Flags

| Flag         | Description                            |
|--------------|----------------------------------------|
| `--target`   | Target IP or domain                    |
| `--network`  | Perform port scanning                  |
| `--web`      | Run web vulnerability checks           |
| `--dir`      | Directory brute-force scan             |
| `--ssl`      | SSL/TLS certificate scan               |
| `--cms`      | CMS/Tech fingerprinting                |
| `--output`   | Save results to specified file         |

---

## 📂 Sample Output

```text
--- TARGET ---
http://example.com

--- OPEN PORTS ---
80/tcp - HTTP
443/tcp - HTTPS

--- WEB VULNERABILITIES ---
- Missing Headers: X-Frame-Options, CSP
- Reflected XSS: Not Detected
- Sensitive file: http://example.com/admin/

--- SSL CERT ---
Valid Till: Dec 15, 2025

--- CMS DETECTED ---
WordPress
```

---

