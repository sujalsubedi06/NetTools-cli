```markdown
# PortScout

A modern Python infrastructure analysis toolkit for discovering, inspecting, and reporting on network services and web applications.

![Python](https://img.shields.io/badge/python-3.13%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Version](https://img.shields.io/badge/version-1.0.0-blue)

---

## Overview

PortScout combines network scanning, DNS intelligence, subdomain discovery, web inspection, and automated technical reporting into a single command-line workflow.

Infrastructure assessments typically require juggling several disconnected tools — a port scanner, a DNS lookup utility, a subdomain enumerator, and a separate script to inspect HTTP responses — then manually assembling the results into something readable. PortScout consolidates these steps into one consistent CLI with a shared output format, so a full assessment of a target domain can be run and reported on without switching tools.

It is built for developers, system administrators, and technical users who need a fast, scriptable way to inspect a domain's network and web footprint and produce shareable JSON or HTML output.

---

## Features

### Network Analysis
- TCP port scanning
- Service identification
- Custom port selection
- Concurrent scanning
- Connection timing analysis
- JSON export support

### DNS Intelligence
- DNS record lookup (A, AAAA, MX, TXT, CNAME)
- Reverse DNS lookup
- Record inspection
- Domain validation

### Subdomain Discovery
- Subdomain enumeration
- Custom wordlist support
- DNS resolution of discovered names
- Discovery reporting
- JSON export support

### Web Inspection
- HTTP status analysis
- Server identification
- Content type detection
- Response timing
- HTTPS detection
- Configuration analysis
- Security header inspection

### Assessment & Reporting
- Combined multi-module assessment workflow (DNS → Subdomains → Web → Report)
- Structured JSON data exports
- Professional HTML assessment reports

---

## Installation

### Clone the repository

```bash
git clone https://github.com/sujalsubedi06/PortScout.git
cd PortScout
```

### Create a virtual environment

**Linux/macOS**

```bash
python -m venv .venv
source .venv/bin/activate
```

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Install the package

```bash
pip install -e .
```

Verify the installation:

```bash
portscout --version
```

```
PortScout v1.0.0
```

---

## Quick Start

Run a full automated assessment against a target domain:

```bash
portscout assess example.com --output output/example-assessment.json
```

This runs DNS analysis, subdomain discovery, and web inspection in sequence, then writes a structured JSON assessment file containing the collected results.

---

## CLI Usage

### `portscout scan`

TCP port scanning against a target.

```bash
portscout scan example.com
portscout scan example.com --ports 80,443,8080
portscout scan example.com --timeout 5
portscout scan example.com --output output/scan.json
```

### `portscout dns`

DNS record lookups and reverse lookups.

```bash
portscout dns example.com
portscout dns example.com --reverse 8.8.8.8
portscout dns example.com --output output/dns.json
```

### `portscout subdomains`

Subdomain enumeration using a built-in or custom wordlist.

```bash
portscout subdomains example.com
portscout subdomains example.com --wordlist wordlist.txt
portscout subdomains example.com --output output/subdomains.json
```

### `portscout web`

HTTP/HTTPS inspection of a target's web application.

```bash
portscout web example.com
portscout web example.com --output output/web.json
```

### `portscout assess`

Runs DNS, subdomain, and web modules together and produces a combined assessment.

```bash
portscout assess example.com
portscout assess example.com --output output/example-assessment.json
```

---

## Architecture

```
PortScout
├── CLI            Command interface (Typer-based)
├── Scanner        TCP scanning engine
├── DNS            DNS resolution engine
├── Subdomains     Domain discovery engine
├── Web            Application inspection
├── Report         HTML report generation
└── Core           Output handling, console utilities, shared components
```

Each module is independently invokable from the CLI, and the `assess` command orchestrates them into a single pipeline: **DNS Analysis → Subdomain Discovery → Web Inspection → Technical Assessment Report**.

---

## Project Structure

```
PortScout/
├── src/
│   └── portscout/
│       ├── cli/            # Command interface (scan, dns, subdomains, web, assess)
│       ├── core/           # Shared utilities and output handling
│       ├── scanner/        # TCP scanning engine
│       ├── dns/            # DNS resolution
│       ├── subdomains/     # Subdomain enumeration
│       ├── web/            # Web/HTTP inspection
│       └── report/         # HTML report generation
├── tests/                  # Test suite
├── output/                 # Default location for JSON/HTML output
├── pyproject.toml
└── README.md
```

---

## Output & Reports

PortScout supports structured, machine-readable JSON exports and can generate human-readable technical reports from assessment data.

**JSON output** — every module (`scan`, `dns`, `subdomains`, `web`, `assess`) supports `--output` to write results as JSON, suitable for further scripting or ingestion into other tools.

**HTML reports** — the `report` module renders assessment data into a professional HTML report using the templates under `src/portscout/report/templates/`.

Example output layout:

```
output/
├── example-assessment.json
└── reports/
    └── assessment-report.html
```

A generated report typically includes:

- Target information
- DNS information
- Web application details
- Configuration observations
- Technical findings
- Raw collected data

---

## Development

Install development dependencies:

```bash
pip install -e ".[dev]"
```

Development dependencies include `pytest`, `pytest-cov`, `ruff`, `mypy`, and `pre-commit`.

### Code quality tools

Lint with Ruff:

```bash
ruff check .
```

Type-check with mypy (strict mode):

```bash
mypy src
```

### Running tests

```bash
python -m pytest
```

---

## Testing

The test suite covers:

- DNS resolution and failure handling
- Subdomain discovery
- Web inspection
- General error handling across modules

Run the full suite with:

```bash
python -m pytest
```

---

## Roadmap

### v1.1
- PDF report export
- Improved report themes
- Expanded DNS record support
- Additional service detection

### v1.2
- REST API
- Database storage
- Background assessments
- Historical reports / dashboard

### v2.0
- Plugin system
- Distributed scanning
- Advanced visualization
- Infrastructure monitoring

---

## Contributing

Contributions are welcome. Typical workflow:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Make your changes and add tests
4. Run tests locally
5. Open a pull request describing the change

---

## Technology Stack

- Python 3.13+
- [Typer](https://typer.tiangolo.com/) — CLI framework
- [Rich](https://github.com/Textualize/rich) — terminal output
- [Requests](https://requests.readthedocs.io/) — HTTP client
- [dnspython](https://www.dnspython.org/) — DNS resolution
- [Pytest](https://pytest.org/) — testing

---

## License

Released under the [MIT License](LICENSE).

---

## Author

**Sujal Subedi**
GitHub: [github.com/sujalsubedi06](https://github.com/sujalsubedi06)
```