"""
Security report generator.
"""

from __future__ import annotations

import json
from pathlib import Path

from portscout.report.models import SecurityReport


class ReportGenerator:
    """
    Generate security reports from JSON data.
    """

    def load_json(
        self,
        path: str | Path,
    ) -> dict:
        """
        Load JSON report data.
        """

        return json.loads(
            Path(path).read_text(
                encoding="utf-8",
            )
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
        Render HTML report.
        """

        return f"""
<!DOCTYPE html>
<html>
<head>
<title>PortScout Security Report</title>
<style>
body {{
    font-family: Arial, sans-serif;
    margin: 40px;
}}

h1 {{
    color: #00aaff;
}}

pre {{
    background: #111;
    color: #eee;
    padding: 20px;
    border-radius: 8px;
}}
</style>
</head>

<body>

<h1>PortScout Security Report</h1>

<h2>Target</h2>
<p>{report.target}</p>

<h2>Data</h2>

<pre>
{json.dumps(
    report.sections,
    indent=4
)}
</pre>

</body>
</html>
"""