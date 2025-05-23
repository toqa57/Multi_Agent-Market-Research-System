import pandas as pd
import json
from typing import Dict, List
from pathlib import Path
from config.logging_config import logger


def clean_job_data(raw_data: List[Dict]) -> pd.DataFrame:
    """Clean and structure raw job posting data"""
    try:
        df = pd.DataFrame(raw_data)

        # Standardize column names
        df.columns = df.columns.str.lower().str.replace(' ', '_')

        # Handle missing values
        df = df.fillna({
            'skills': 'Unknown',
            'location': 'Remote'
        })

        logger.info(f"Cleaned {len(df)} job records")
        return df

    except Exception as e:
        logger.error(f"Data cleaning failed: {str(e)}")
        raise


def extract_skills(description: str) -> List[str]:
    """Extract skills from job description text"""
    skill_keywords = [
        'python', 'tensorflow', 'pytorch',
        'machine learning', 'deep learning', 'nlp'
    ]

    return [skill for skill in skill_keywords
            if skill.lower() in description.lower()]