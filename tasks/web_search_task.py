from crewai import Task
from typing import Optional
from config.logging_config import logger

def create_web_search_task(agent, context: Optional[list] = None):
    """Create task for searching job postings"""
    try:
        return Task(
            description="""Search LinkedIn, Bayt, and Wuzzuf for AI/ML jobs in MENA.
                        Find at least 50 recent postings.""",
            expected_output="List of job posting URLs",
            agent=agent,
            context=context,
            async_execution=True  # Enable parallel execution
        )
    except Exception as e:
        logger.error(f"Failed to create search task: {str(e)}")
        raise