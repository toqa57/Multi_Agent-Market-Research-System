from crewai import Task
from config.logging_config import logger

def create_trend_analysis_task(agent, context: list):
    """Create task for analyzing job market trends"""
    try:
        return Task(
            description="""Analyze job data to identify:
                        1. Top 10 job titles
                        2. Most demanded skills
                        3. Geographic distribution""",
            expected_output="Analysis report with key insights",
            agent=agent,
            context=context
        )
    except Exception as e:
        logger.error(f"Failed to create analysis task: {str(e)}")
        raise