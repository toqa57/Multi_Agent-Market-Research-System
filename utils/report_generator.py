from typing import Dict
import markdown
import pdfkit
from datetime import datetime
from pathlib import Path
from config.logging_config import logger


def generate_markdown_report(data: Dict, output_path: str) -> str:
    """Generate markdown format report"""
    try:
        report = f"""# AI/ML Job Market Report - {datetime.now().strftime('%B %Y')}

## Top Job Titles
"""
        for title, count in data.get('top_titles', {}).items():
            report += f"- {title}: {count} postings\n"

        # Add more sections as needed...

        Path(output_path).write_text(report)
        logger.info(f"Report generated at {output_path}")
        return report

    except Exception as e:
        logger.error(f"Report generation failed: {str(e)}")
        raise


def convert_to_pdf(markdown_file: str, output_path: str):
    """Convert markdown report to PDF"""
    try:
        html = markdown.markdown(Path(markdown_file).read_text())
        pdfkit.from_string(html, output_path)
        logger.info(f"PDF generated at {output_path}")
    except Exception as e:
        logger.error(f"PDF conversion failed: {str(e)}")
        raise