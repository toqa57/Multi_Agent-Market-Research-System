from crewai import Task
from config.logging_config import logger
from typing import Optional

def create_data_extraction_task(agent, context: Optional[list] = None):
    """Create task for extracting job details"""
    try:
        return Task(
            description="""Extract job title, skills, company, and location
                        from each job posting URL.""",
            expected_output="Structured data in JSON format",
            agent=agent,
            context=context,
            output_file="data/processed/jobs.json"
        )
    except Exception as e:
        logger.error(f"Failed to create extraction task: {str(e)}")
        raise