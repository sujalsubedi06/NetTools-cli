# PortScout

A modern Python infrastructure analysis toolkit for discovering, inspecting, and reporting on network services and web applications.

PortScout combines network scanning, DNS intelligence, subdomain discovery, web inspection, and automated technical reports into a single command-line workflow.

Built with Python, PortScout focuses on providing a clean, extensible, and developer-friendly approach to infrastructure visibility and technical assessment.

---

# Features

## Network Analysis

PortScout provides TCP-based network inspection capabilities:

- TCP port scanning
- Service identification
- Custom port selection
- Concurrent scanning
- Connection timing analysis
- JSON export support

Example:

```bash
portscout scan example.com
```

---

## DNS Intelligence

Analyze domain DNS infrastructure:

Supported operations:

- DNS record lookup
- Reverse DNS lookup
- Record inspection
- Domain validation

Supported record types:

- A
- AAAA
- MX
- TXT
- CNAME

Example:

```bash
portscout dns example.com
```

Reverse lookup:

```bash
portscout dns example.com --reverse 8.8.8.8
```

---

## Subdomain Discovery

Discover related domain infrastructure:

Features:

- Subdomain enumeration
- Custom wordlists
- DNS resolution
- Discovery reporting
- JSON export support

Example:

```bash
portscout subdomains example.com
```

Custom wordlist:

```bash
portscout subdomains example.com --wordlist domains.txt
```

---

## Web Inspection

Analyze web applications and services:

Features:

- HTTP status analysis
- Server identification
- Content type detection
- Response timing
- HTTPS detection
- Configuration analysis
- Security header inspection

Example:

```bash
portscout web example.com
```

---

## Automated Assessment

Run multiple analysis modules together:

```bash
portscout assess example.com
```

Assessment workflow:

```
Target Domain

      |
      v

DNS Analysis

      |
      v

Subdomain Discovery

      |
      v

Web Inspection

      |
      v

Technical Assessment Report
```

Save assessment data:

```bash
portscout assess example.com \
--output output/example-assessment.json
```

---

# Reporting

PortScout generates structured technical reports.

Supported formats:

- JSON data exports
- Professional HTML assessment reports

Reports include:

- Target information
- DNS information
- Web application details
- Configuration observations
- Technical findings
- Raw collected data

Example output:

```
output/

├── example-assessment.json

└── reports/

    └── security-report.html
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/sujalsubedi06/PortScout.git

cd PortScout
```

---

## Create Virtual Environment

Linux/macOS:

```bash
python -m venv .venv

source .venv/bin/activate
```

Windows:

```bash
python -m venv .venv

.venv\Scripts\activate
```

---

## Install Package

Install PortScout:

```bash
pip install -e .
```

---

# Usage

## Check Version

```bash
portscout --version
```

Example:

```
PortScout v1.0.0
```

---

# Command Reference

## Scan

Basic scan:

```bash
portscout scan example.com
```

Custom ports:

```bash
portscout scan example.com --ports 80,443,8080
```

Custom timeout:

```bash
portscout scan example.com --timeout 5
```

JSON output:

```bash
portscout scan example.com \
--output output/scan.json
```

---

## DNS

Lookup DNS records:

```bash
portscout dns example.com
```

Save output:

```bash
portscout dns example.com \
--output output/dns.json
```

---

## Subdomains

Enumerate subdomains:

```bash
portscout subdomains example.com
```

Custom wordlist:

```bash
portscout subdomains example.com \
--wordlist wordlist.txt
```

Save output:

```bash
portscout subdomains example.com \
--output output/subdomains.json
```

---

## Web

Inspect website:

```bash
portscout web example.com
```

Save output:

```bash
portscout web example.com \
--output output/web.json
```

---

## Assessment

Complete analysis:

```bash
portscout assess example.com
```

Save assessment:

```bash
portscout assess example.com \
--output output/example-assessment.json
```

---

# Architecture

```
PortScout

├── CLI
│   └── Command interface
│
├── Scanner
│   └── TCP scanning engine
│
├── DNS
│   └── DNS resolution engine
│
├── Subdomains
│   └── Domain discovery engine
│
├── Web
│   └── Application inspection
│
├── Reports
│   └── HTML report generation
│
└── Core
    ├── Output handling
    ├── Console utilities
    └── Shared components
```

---

# Project Structure

```
PortScout/

├── src/

│   └── portscout/

│       ├── cli/

│       ├── scanner/

│       ├── dns/

│       ├── subdomains/

│       ├── web/

│       ├── report/

│       └── core/


├── tests/

├── output/

├── pyproject.toml

└── README.md
```

---

# Development

Install development dependencies:

```bash
pip install -e ".[dev]"
```

Run test suite:

```bash
python -m pytest
```

Expected:

```
All tests passed
```

---

# Testing

PortScout includes automated tests covering:

- DNS resolution
- DNS failures
- Subdomain discovery
- Web inspection
- Error handling

Run:

```bash
python -m pytest
```

---

# Roadmap

Future improvements:

## v1.1

- PDF report export
- Improved report themes
- More DNS record support
- Additional service detection

## v1.2

- REST API
- Database storage
- Background assessments
- Historical reports

## v2

- Plugin system
- Distributed scanning
- Advanced visualization
- Infrastructure monitoring

---

# Technology Stack

Built with:

- Python
- Typer
- Rich
- Requests
- dnspython
- Pytest

---

# Version

Current version:

```
1.0.0
```

---

# License

MIT License

---

# Author

Sujal Subedi

GitHub:

https://github.com/sujalsubedi06