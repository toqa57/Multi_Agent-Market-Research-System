import json
import pandas as pd
from pathlib import Path
import os
from datetime import datetime
from typing import Union, List, Dict, Optional
import logging
import matplotlib.pyplot as plt


class DataManager:
    def __init__(self, base_path: str = "utils/data"):
        """
        Enhanced DataManager that now includes:
        - outputs/reports directory for final reports
        - Integration with main.py
        - Requirements management
        """
        self.base_path = Path(base_path).absolute()
        self.reports_path = Path("outputs/reports").absolute()
        self._setup_logger()
        self._create_full_structure()
        self._verify_write_permissions()

    def _setup_logger(self):
        """Configure comprehensive logging"""
        self.logger = logging.getLogger('DataManager')
        self.logger.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Console handler
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

        # File handler
        log_file = self.base_path.parent / 'data_operations.log'
        fh = logging.FileHandler(log_file)
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def _create_full_structure(self):
        """Create complete directory structure including outputs"""
        # Data directories
        data_structure = {
            'raw': ['linkedin', 'bayt', 'wuzzuf'],
            'processed': [],
            'visualizations': []
        }

        # Output directories
        output_structure = {
            'reports': []
        }

        try:
            # Create data directories
            for main_dir, subdirs in data_structure.items():
                main_dir_path = self.base_path / main_dir
                main_dir_path.mkdir(parents=True, exist_ok=True)
                self.logger.info(f"Created data directory: {main_dir_path}")

                for subdir in subdirs:
                    subdir_path = main_dir_path / subdir
                    subdir_path.mkdir(exist_ok=True)
                    self.logger.info(f"Created data subdirectory: {subdir_path}")

            # Create output directories
            self.reports_path.mkdir(parents=True, exist_ok=True)
            self.logger.info(f"Created reports directory: {self.reports_path}")

        except Exception as e:
            self.logger.error(f"Directory creation failed: {str(e)}")
            raise

    def _verify_write_permissions(self):
        """Verify write access to all critical directories"""
        test_locations = [
            self.base_path / 'raw' / 'linkedin',
            self.base_path / 'processed',
            self.reports_path
        ]

        for location in test_locations:
            test_file = location / 'permission_test.tmp'
            try:
                test_file.write_text('test')
                test_file.unlink()
                self.logger.info(f"Write verified in: {location}")
            except Exception as e:
                self.logger.critical(f"Write failed in {location}: {str(e)}")
                raise

    def generate_report(self, analysis_results: Dict, report_name: str) -> Path:
        """
        Generate and save a comprehensive report

        Args:
            analysis_results: Dictionary containing analysis data
            report_name: Base name for the report file

        Returns:
            Path to saved report
        """
        try:
            # Create markdown content
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            md_content = f"# AI/ML Jobs Market Report\n\n"
            md_content += f"**Generated**: {timestamp}\n\n"

            # Add analysis sections
            md_content += "## Top Job Titles\n"
            for title, count in analysis_results.get('top_titles', {}).items():
                md_content += f"- {title}: {count} postings\n"

            md_content += "\n## Skill Distribution\n"
            for skill, freq in analysis_results.get('top_skills', {}).items():
                md_content += f"- {skill} ({freq} occurrences)\n"

            # Save markdown file
            report_path = self.reports_path / f"{report_name}.md"
            report_path.write_text(md_content)

            self.logger.info(f"Report saved to: {report_path}")
            return report_path

        except Exception as e:
            self.logger.error(f"Report generation failed: {str(e)}")
            raise

    # ... [Previous methods remain unchanged: save_raw_data, save_processed_data, etc.] ...

    def get_requirements(self) -> List[str]:
        """
        Get list of required Python packages

        Returns:
            List of package requirements
        """
        return [
            "pandas>=1.3.0",
            "matplotlib>=3.4.0",
            "python-dotenv>=0.19.0",
            "langchain>=0.0.200",
            "crewai>=0.1.0"
        ]

    def generate_requirements_file(self):
        """Generate requirements.txt in project root"""
        requirements_path = Path("requirements.txt")
        requirements_path.write_text("\n".join(self.get_requirements()))
        self.logger.info(f"Generated requirements file at: {requirements_path}")