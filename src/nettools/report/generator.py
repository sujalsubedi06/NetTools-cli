"""
Technical assessment report generator.
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from nettools import __version__
from nettools.report.models import SecurityReport


class ReportGenerator:
    """
    Generate professional HTML reports.
    """

    def load_json(
        self,
        path: str | Path,
    ) -> dict:
        """
        Load JSON data.
        """

        return json.loads(
            Path(path).read_text(
                encoding="utf-8",
            )
        )

    def load_template(self) -> str:
        """
        Load HTML template.
        """

        template = Path(__file__).parent / "templates" / "report.html"

        return template.read_text(
            encoding="utf-8",
        )

    def generate(
        self,
        input_path: str | Path,
        output_path: str | Path,
    ) -> Path:
        """
        Generate HTML report.
        """

        data = self.load_json(
            input_path,
        )

        report = SecurityReport(
            target=str(input_path),
            sections=data,
        )

        html = self.render(
            report,
        )

        output = Path(output_path)

        output.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        output.write_text(
            html,
            encoding="utf-8",
        )

        return output

    def render(
        self,
        report: SecurityReport,
    ) -> str:
        """
        Render HTML from template.
        """

        template = self.load_template()

        data = report.sections

        web = data.get(
            "web_info",
            {},
        )

        security = data.get(
            "security",
            {},
        )

        web_rows = ""

        fields = {
            "URL": web.get("url"),
            "Status": web.get("status_code"),
            "Title": web.get("title"),
            "Server": web.get("server"),
            "Content Type": web.get("content_type"),
            "HTTPS": web.get("https"),
            "Redirects": web.get("redirects"),
            "Response Time": web.get("response_time"),
        }

        for key, value in fields.items():
            web_rows += f"""
<tr>
<td>{key}</td>
<td>{value}</td>
</tr>
"""

        missing_headers = security.get(
            "missing_headers",
            [],
        )

        findings = ""

        if missing_headers:
            for item in missing_headers:
                findings += f"""
<li>{item}</li>
"""
        else:
            findings = """
<li>No configuration issues detected.</li>
"""

        html = template.replace(
            "{{ target }}",
            str(web.get("url", report.target)),
        )

        html = html.replace(
            "{{ generated_at }}",
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S",
            ),
        )

        html = html.replace(
            "{{ version }}",
            __version__,
        )

        html = html.replace(
            "{{ web_rows }}",
            web_rows,
        )

        html = html.replace(
            "{{ security_score }}",
            str(
                security.get(
                    "score",
                    "N/A",
                )
            ),
        )

        html = html.replace(
            "{{ https_status }}",
            ("Enabled" if security.get("https") else "Disabled"),
        )

        html = html.replace(
            "{{ findings }}",
            findings,
        )

        html = html.replace(
            "{{ raw_data }}",
            json.dumps(
                data,
                indent=4,
            ),
        )

        return html
