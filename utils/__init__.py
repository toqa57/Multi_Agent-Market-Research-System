# utils/__init__.py

from utils.data_processing import clean_job_data, extract_skills
from utils.visualization import plot_job_trends, create_skill_heatmap
from utils.report_generator import generate_markdown_report, convert_to_pdf
from pathlib import Path



__all__ = [
    'clean_job_data',
    'extract_skills',
    'plot_job_trends',
    'create_skill_heatmap',
    'generate_markdown_report',
    'convert_to_pdf'
]

class DataManager:
    def __init__(self, base_path: str = "data"):
        """
        Robust data storage manager with error handling and verification

        Args:
            base_path: Relative path to data directory
        """
        self.base_path = Path(__file__).resolve().parent / base_path
        self._setup_directories()
        self._verify_write_permissions()