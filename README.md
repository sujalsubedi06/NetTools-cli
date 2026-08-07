# NetTools CLI

**A modern Python network reconnaissance toolkit.**

[![Python Version](https://img.shields.io/badge/python-3.13%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Package Status](https://img.shields.io/badge/status-active-brightgreen.svg)](https://github.com/sujalsubedi06/nettools-cli)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](https://github.com/sujalsubedi06/nettools-cli/actions)
[![PyPI Version](https://img.shields.io/pypi/v/nettools-cli.svg)](https://pypi.org/project/nettools-cli/)

---

## Overview

NetTools CLI is a modular Python command-line toolkit for **authorized** network diagnostics and service discovery. It brings together several common reconnaissance workflows — port scanning, DNS analysis, subdomain enumeration, web inspection, and assessment reporting — into a single, consistent CLI built on top of [Typer](https://typer.tiangolo.com/) and [Rich](https://rich.readthedocs.io/).

NetTools CLI is intended for:

- **Security teams and penetration testers** performing authorized assessments
- **System administrators** auditing infrastructure they manage
- **DevOps and network engineers** diagnosing connectivity and DNS issues
- **Students and researchers** learning about network diagnostics in a controlled, ethical context

NetTools CLI is not a hacking tool, and it is not designed to bypass authorization, evade detection, or exploit vulnerabilities. It is a diagnostics and reporting utility intended to help authorized users understand the state of systems they are responsible for or have explicit permission to test.

---

## Features

- **TCP port scanning** — Identify open, closed, and filtered TCP ports on target hosts
- **DNS lookup** — Query common DNS record types (A, AAAA, MX, TXT, NS, CNAME, and more)
- **Subdomain enumeration** — Discover subdomains using wordlist-based and passive techniques
- **Website inspection** — Inspect HTTP/HTTPS endpoints, headers, TLS certificate details, and basic metadata
- **Unified assessment workflow** — Run scan, DNS, subdomain, and web checks together in a single pass
- **HTML report generation** — Produce clean, shareable HTML reports summarizing findings
- **JSON output support** — Machine-readable output for every command, suitable for automation and pipelines
- **Modular architecture** — Each capability lives in its own module, making the codebase easy to extend and maintain

---

## Architecture

NetTools CLI follows a `src`-based package layout, keeping the installable package isolated from project tooling and tests.

```
nettools-cli/
├── src/
│   └── nettools/
│       ├── __init__.py
│       ├── cli/
│       │   ├── app.py
│       │   ├── scan.py
│       │   ├── dns.py
│       │   ├── subdomains.py
│       │   ├── web.py
│       │   ├── assess.py
│       │   └── report.py
│       │
│       ├── core/
│       ├── scanner/
│       ├── dns/
│       ├── subdomains/
│       ├── web/
│       └── report/
```

Each command module is responsible for a single capability and exposes a clear, testable interface. Shared logic (networking primitives, formatting, configuration) lives under `core/` and `output/` so commands stay thin and consistent.

---

## Installation

### From PyPI

```bash
pip install nettools-cli
```

### From source

```bash
git clone https://github.com/sujalsubedi06/nettools-cli
cd nettools-cli
pip install -e .
```

NetTools CLI requires **Python 3.13 or later**.

---

## Usage

View all available commands:

```bash
nettools --help
```

Scan common TCP ports on a target:

```bash
nettools scan example.com
```

Perform DNS lookups:

```bash
nettools dns example.com
```

Run a full assessment (scan, DNS, subdomains, and web inspection together):

```bash
nettools assess example.com
```

Generate an HTML report from previous results:

```bash
nettools report --help
```

Other available commands:

```bash
nettools subdomains example.com
nettools web example.com
nettools version
```

Most commands support a `--json` flag for machine-readable output, suitable for scripting or integration with other tools:

```bash
nettools scan example.com --json
```

---

## Configuration

NetTools CLI can be configured via a project-level configuration file, environment variables, or command-line flags, in increasing order of precedence.

- **Configuration file**: `nettools.toml` in the current working directory, or a path passed via `--config`
- **Environment variables**: prefixed with `NETTOOLS_` (e.g. `NETTOOLS_TIMEOUT`, `NETTOOLS_MAX_WORKERS`)
- **CLI flags**: passed directly to individual commands (e.g. `--timeout`, `--ports`, `--output`)

Common configurable options include:

| Option | Description | Default |
|---|---|---|
| `timeout` | Per-connection timeout in seconds | `3` |
| `max_workers` | Concurrent worker threads/processes | `50` |
| `ports` | Port range or list to scan | Common ports (top 1000) |
| `output_dir` | Directory for reports and JSON output | `./nettools-output` |
| `wordlist` | Wordlist path for subdomain enumeration | Bundled default wordlist |

Refer to `nettools <command> --help` for the full set of options available on each command.

---

## Development Setup

Clone the repository and set up a local development environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

pip install -e ".[dev]"
```

Run the test suite:

```bash
pytest -v
```

Run linting and type checks:

```bash
ruff check .
ruff format .
mypy
```

---

## Testing

NetTools CLI uses [pytest](https://docs.pytest.org/) for automated testing, with unit tests covering individual modules and integration tests covering end-to-end CLI behavior against controlled, local test fixtures. Networking calls in tests are mocked or run against local/loopback targets to keep the suite deterministic and safe to run in CI.

To run the full suite with verbose output:

```bash
pytest -v
```

Contributions are expected to include appropriate test coverage for new functionality. Continuous integration runs the test suite, `ruff check`, and `mypy` on every pull request.

---

## Roadmap

Planned and potential future improvements include:

- Asynchronous scanning engine for improved performance on large port ranges
- Additional DNS record types and DNSSEC validation checks
- Plugin system for custom assessment modules
- PDF export for assessment reports
- Configurable scan profiles (fast, thorough, stealth-safe timing)
- Expanded passive subdomain enumeration sources
- Structured logging and verbosity controls

Roadmap items are tracked and discussed in the project's GitHub Issues.

---

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:

- Setting up your development environment
- Coding standards and style (enforced via Ruff and Mypy)
- Commit message conventions
- Submitting pull requests and what reviewers look for

---

## Security

If you discover a security vulnerability in NetTools CLI itself, please **do not open a public issue**. Instead, follow the responsible disclosure process described in [SECURITY.md](SECURITY.md).

---

## License

NetTools CLI is released under the [MIT License](LICENSE).

---

## Responsible Usage

NetTools CLI is a diagnostic and reporting tool intended strictly for **authorized** use.

- Only use NetTools CLI against systems, networks, and domains that you own, or for which you have explicit, documented permission to test.
- NetTools CLI is intended for **authorized diagnostics, auditing, and educational purposes only**.
- Unauthorized scanning, enumeration, or assessment of systems you do not own or have permission to test may violate laws and regulations in your jurisdiction, as well as the terms of service of the target system's provider.
- Users are solely responsible for ensuring their use of NetTools CLI complies with all applicable laws and any agreements governing the systems being tested.

The maintainers of NetTools CLI assume no liability for misuse of this software.