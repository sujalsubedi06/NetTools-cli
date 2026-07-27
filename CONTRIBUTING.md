# Contributing to nettools

Thank you for your interest in contributing to **nettools** — a modern Python network reconnaissance toolkit for authorized network diagnostics, service discovery, DNS analysis, and web asset inspection.

nettools is built for security professionals, network administrators, and engineers who need reliable, well-tested tooling for diagnosing and understanding networks they own or are explicitly authorized to assess. This document explains how to get involved, set up your development environment, and submit high-quality contributions.

We welcome contributions of all sizes, from fixing a typo in the documentation to implementing a new scanning module. Please take a moment to read through this guide before opening an issue or pull request.

---

## 1. Introduction

nettools follows standard open-source contribution practices. Whether you're fixing a bug, improving documentation, adding tests, or proposing a new feature, this guide will help you contribute effectively and in a way that aligns with the project's goals and quality standards.

By participating in this project, you agree to abide by our [Code of Conduct](#15-code-of-conduct) and to use nettools — and any code you contribute to it — strictly for **authorized, legal, and ethical purposes**.

---

## 2. Ways to Contribute

There are many ways to contribute to nettools, including:

- **Bug reports** — Identifying and reporting issues with clear reproduction steps.
- **Bug fixes** — Submitting pull requests that resolve open issues.
- **New features** — Proposing and implementing new diagnostic, discovery, or inspection capabilities.
- **Documentation** — Improving README content, docstrings, usage guides, and examples.
- **Testing** — Adding or improving test coverage with `pytest`.
- **Code quality** — Refactoring, improving type annotations, or addressing linting issues.
- **Triage** — Helping review and label issues, or reproducing reported bugs.
- **Discussions** — Participating in design discussions for upcoming features.

If you're unsure whether a contribution is a good fit, feel free to open an issue first to discuss it.

---

## 3. Development Environment Setup

nettools requires:

- **Python 3.13+**
- **pip** (latest version recommended)
- **Git**

The project uses a `src`-layout modular package structure and **Hatchling** as its build backend, with `pyproject.toml` as the single source of build and dependency configuration.

---

## 4. Cloning the Repository

Fork the repository on GitHub, then clone your fork locally:

```bash
git clone https://github.com/<your-username>/nettools.git
cd nettools
```

If you plan to contribute regularly, add the upstream repository as a remote so you can keep your fork in sync:

```bash
git remote add upstream https://github.com/<original-org>/nettools.git
git fetch upstream
```

---

## 5. Virtual Environment Setup

It is strongly recommended to use an isolated virtual environment for development.

```bash
python3.13 -m venv .venv
source .venv/bin/activate      # On Linux/macOS
.venv\Scripts\activate         # On Windows
```

Ensure `pip` is up to date before installing dependencies:

```bash
python -m pip install --upgrade pip
```

---

## 6. Installing Development Dependencies

nettools uses extras defined in `pyproject.toml` to manage development tooling. Install the project in editable mode along with development dependencies:

```bash
pip install -e ".[dev]"
```

This installs nettools itself (editable, so your changes take effect immediately), along with tools such as `pytest`, `ruff`, and `mypy`.

---

## 7. Running Tests

nettools uses **pytest** for its test suite. All new features and bug fixes should include appropriate test coverage.

Run the full test suite with verbose output:

```bash
pytest -v
```

Before submitting a pull request, please ensure:

- All existing tests pass.
- New functionality includes corresponding unit tests.
- Bug fixes include a regression test where practical.

---

## 8. Code Formatting and Linting

nettools uses **ruff** for both linting and formatting to maintain a consistent, clean codebase.

Check for lint issues:

```bash
ruff check .
```

Automatically format code:

```bash
ruff format .
```

Please run both commands before committing. Pull requests with unresolved lint errors or inconsistent formatting may be asked for revision.

---

## 9. Type Checking

nettools maintains type-annotated code and uses **mypy** for static type checking.

```bash
mypy
```

All new code should include type annotations, and contributions should not introduce new `mypy` errors. If you must use `# type: ignore`, include a brief comment explaining why.

---

## 10. Branch Naming Guidelines

Use short, descriptive branch names prefixed by category:

| Prefix      | Purpose                              | Example                          |
|-------------|---------------------------------------|-----------------------------------|
| `feature/`  | New features                          | `feature/dns-record-inspector`   |
| `fix/`      | Bug fixes                             | `fix/tcp-scan-timeout`           |
| `docs/`     | Documentation-only changes            | `docs/update-cli-usage`          |
| `refactor/` | Internal refactors, no behavior change| `refactor/scanner-module`        |
| `test/`     | Test-only additions or improvements   | `test/add-dns-resolver-tests`    |
| `chore/`    | Tooling, CI, dependency updates       | `chore/bump-ruff-version`        |

Branch off the latest `main` and keep branches focused on a single logical change.

---

## 11. Commit Message Conventions

nettools follows a lightweight [Conventional Commits](https://www.conventionalcommits.org/) style:

```
<type>(<scope>): <short summary>

[optional body]

[optional footer]
```

**Common types:** `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `perf`, `style`

**Examples:**

```
feat(dns): add support for reverse DNS lookups
fix(scanner): correct timeout handling on slow hosts
docs(readme): clarify authorized-use requirements
test(webinspect): add coverage for redirect handling
```

Guidelines:

- Use the imperative mood ("add", not "added" or "adds").
- Keep the summary line under 72 characters.
- Reference related issues in the footer, e.g. `Closes #42`.

---

## 12. Pull Request Guidelines

Before opening a pull request:

1. Ensure your branch is up to date with `main`.
2. Run the full quality checklist:
   ```bash
   ruff check .
   ruff format .
   mypy
   pytest -v
   ```
3. Update documentation and docstrings relevant to your change.
4. Add or update tests as needed.

**When submitting a PR:**

- Use a clear, descriptive title.
- Fill out the PR template, including a summary of the change and its motivation.
- Link related issues (e.g., `Closes #123`).
- Keep PRs focused — avoid bundling unrelated changes.
- Be responsive to review feedback; PRs may go through several rounds of review before merging.

Maintainers may request changes, ask clarifying questions, or suggest alternative approaches. This is a normal part of maintaining code quality and project consistency.

---

## 13. Issue Reporting Guidelines

When reporting a bug, please include:

- **nettools version** (`nettools --version`)
- **Python version** and operating system
- **Steps to reproduce** the issue
- **Expected behavior** vs. **actual behavior**
- Relevant logs, error messages, or stack traces (with sensitive network details redacted)

For feature requests, please describe:

- The problem or use case you're trying to solve
- Any proposed approach or API design
- Whether you're willing to help implement it

Please search existing issues before opening a new one to avoid duplicates.

---

## 14. Security and Responsible Usage Guidelines

nettools is designed **exclusively for authorized network diagnostics** — including but not limited to authorized penetration testing engagements, internal infrastructure audits, DNS troubleshooting, and asset inventory on networks and systems you own or have explicit, documented permission to test.

**Contributors must adhere to the following principles:**

- **No unauthorized scanning.** Do not use nettools, or contribute features intended to facilitate use, against systems or networks without explicit authorization from their owner.
- **No offensive tooling.** nettools is a diagnostic and discovery toolkit, not an exploitation or attack framework. Contributions that add exploitation, credential brute-forcing, denial-of-service, or similarly offensive capabilities will not be accepted.
- **Responsible defaults.** New scanning or discovery features should include sane rate limits, timeouts, and safeguards to minimize unintended impact on target systems.
- **Vulnerability disclosure.** If you discover a security vulnerability in nettools itself, please **do not** open a public issue. Instead, report it privately by emailing the maintainers (see `SECURITY.md` if present in the repository, or contact the maintainers directly). We will work with you to assess and address the issue promptly.
- **Legal compliance.** Contributors are responsible for ensuring their use and testing of nettools complies with all applicable laws and regulations in their jurisdiction.

By contributing to this project, you affirm that your contributions are intended to support legitimate, authorized diagnostic use cases.

---

## 15. Code of Conduct

This project adheres to a Code of Conduct that we expect all contributors and community members to follow. Please read [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md) before participating.

In short: be respectful, be constructive, and help us maintain a welcoming environment for contributors of all backgrounds and experience levels.

---

## Questions?

If you have questions that aren't covered here, feel free to open a [discussion](../../discussions) or an issue. Thank you for helping make nettools better!