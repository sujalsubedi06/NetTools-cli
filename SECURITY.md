# Security Policy

## 1. Introduction

The nettools team takes the security of the project — and the responsible use of the tool itself — seriously. nettools is a network reconnaissance toolkit built for **authorized** network diagnostics, service discovery, DNS analysis, and web asset inspection. Because it interacts directly with network infrastructure, maintaining a secure, well-audited codebase and a clear reporting process is a top priority for the project.

This document describes which versions of nettools receive security updates, how to report a vulnerability, what to expect from maintainers during the process, and the responsible usage principles that govern this project.

---

## 2. Supported Versions

Security updates are provided for the following versions of nettools. We recommend always running the latest release.

| Version        | Supported          |
|----------------|---------------------|
| Latest release (`main`) | :white_check_mark: |
| Previous minor release  | :white_check_mark: |
| Older releases          | :x:                 |
| Pre-release / dev builds | :warning: Best-effort only |

As nettools is an actively developed project, the supported version window may be adjusted as the release cadence matures. Any changes to this policy will be reflected in this document.

---

## 3. Vulnerability Reporting Process

If you discover a security vulnerability in nettools — whether in the core codebase, a bundled module, packaging/build configuration, or a dependency — please report it **privately**. Do **not** open a public GitHub issue, pull request, or discussion thread for security vulnerabilities, as this could put users at risk before a fix is available.

We follow a coordinated disclosure process:

1. You report the issue privately (see [Section 4](#4-how-to-report-security-issues)).
2. Maintainers acknowledge and investigate the report.
3. A fix is developed and tested privately.
4. A new release is published along with a security advisory.
5. Public disclosure occurs after a fix is available, with credit to the reporter (if desired).

---

## 4. How to Report Security Issues

Please report vulnerabilities using one of the following private channels:

- **GitHub Private Vulnerability Reporting**: Use the "Report a vulnerability" option under the repository's **Security** tab (preferred method, as it keeps the report and discussion confidential within GitHub).
- **Email**: If GitHub Private Vulnerability Reporting is unavailable to you, contact the maintainers directly at the security contact email listed in the repository's profile or `pyproject.toml` metadata.

Please **do not** disclose the vulnerability publicly (including on social media, blog posts, or public forums) until a fix has been released and coordinated disclosure has occurred.

---

## 5. Information to Include in Reports

To help us triage and resolve the issue as quickly as possible, please include:

- **A clear description** of the vulnerability and its potential impact.
- **Affected version(s)** of nettools.
- **Steps to reproduce**, including any relevant configuration, command-line invocation, or code snippet.
- **Environment details** (Python version, operating system, installation method).
- **Proof-of-concept code**, if applicable — please keep any PoC scoped to demonstrating the issue in a controlled, non-destructive environment.
- Any **suggested remediation** or patch, if you have one.
- Whether the issue has been shared with any other party.

Reports with clear reproduction steps are typically resolved faster.

---

## 6. Responsible Disclosure Guidelines

We ask that security researchers and community members:

- Give maintainers a reasonable period to investigate and address the issue before any public disclosure (typically **90 days**, or sooner once a fix is released).
- Avoid accessing, modifying, or exfiltrating data that does not belong to you while investigating a vulnerability.
- Avoid testing vulnerabilities against systems, networks, or infrastructure you do not own or have explicit authorization to test — this includes any live systems that may be running nettools.
- Act in good faith and avoid actions that could degrade the experience, privacy, or security of other users or systems.

We are happy to credit researchers who follow responsible disclosure practices in our release notes and security advisories, unless anonymity is requested.

---

## 7. Maintainer Response Process

Upon receiving a vulnerability report, maintainers will generally follow this timeline:

| Stage                          | Target Timeframe          |
|---------------------------------|----------------------------|
| Initial acknowledgment          | Within 3 business days     |
| Preliminary assessment          | Within 7 business days     |
| Status updates to reporter      | At least every 14 days until resolved |
| Fix development & testing       | Varies by severity and complexity |
| Release and public advisory     | As soon as a validated fix is available |

Severity will be assessed using common industry frameworks (e.g., CVSS) to help prioritize response efforts. Critical vulnerabilities affecting the security or integrity of user systems will be prioritized for expedited patching.

---

## 8. Scope of Security Concerns

**In scope** for security reports include, but are not limited to:

- Remote code execution or arbitrary code execution vulnerabilities.
- Vulnerabilities allowing unauthorized access to a user's local system or data.
- Flaws in dependency handling that could introduce supply-chain risk (e.g., dependency confusion, unpinned/malicious packages).
- Insecure defaults that could cause unintended or unsafe network behavior.
- Credential, secret, or sensitive-data exposure within logs, output, or storage.
- Vulnerabilities in the build, packaging, or release pipeline (e.g., PyPI publishing workflow).
- Issues allowing nettools's own functionality to be abused in ways that bypass intended safeguards (e.g., rate limiting, authorization checks within the tool itself).

**Out of scope** includes:

- Vulnerabilities in third-party networks or systems discovered *using* nettools — these should be reported to the owner of that system, not to the nettools project.
- General misuse of the tool against unauthorized targets (see [Section 9](#9-responsible-usage-policy)).
- Issues that require an already-compromised system or elevated local privileges that are outside nettools's threat model.
- Missing security best practices in unrelated forks or derivative projects.

If you're unsure whether an issue is in scope, please report it privately and we will help clarify.

---

## 9. Responsible Usage Policy

nettools is developed and distributed **exclusively for authorized network diagnostics** — including infrastructure you own, or networks and systems for which you have explicit, documented permission to test (such as authorized penetration testing engagements, internal audits, or DNS/service troubleshooting).

nettools is **not** intended, designed, or maintained as an offensive or exploitation tool. It does not include, and will not accept contributions that add, capabilities such as exploitation frameworks, credential brute-forcing, or denial-of-service functionality.

By using nettools, you agree that:

- You will only scan, probe, or inspect systems and networks you own or are explicitly authorized to test.
- You are solely responsible for ensuring your use of nettools complies with all applicable local, national, and international laws and regulations.
- The maintainers and contributors of nettools bear no responsibility for misuse of the tool by third parties.

Unauthorized scanning of networks or systems may violate computer misuse laws in your jurisdiction. When in doubt, obtain written authorization before use.

---

## 10. Security Update Process

When a security fix is released:

1. A new version is published to PyPI and tagged in the GitHub repository.
2. A **GitHub Security Advisory** is published, describing the vulnerability, affected versions, and remediation steps.
3. Where applicable, a **CVE identifier** will be requested and referenced in the advisory.
4. The `CHANGELOG` and release notes will clearly flag the release as a security update.
5. Users are strongly encouraged to upgrade promptly. Where feasible, maintainers may note mitigations for users who cannot upgrade immediately.

We recommend watching the repository's **Releases** and **Security Advisories** pages to stay informed of security-relevant updates.

---

## Questions

For general (non-security) questions about the project, please use [GitHub Issues](../../issues) or [Discussions](../../discussions). This SECURITY.md is reserved for vulnerability reporting and security policy only.

Thank you for helping keep nettools and its users secure.