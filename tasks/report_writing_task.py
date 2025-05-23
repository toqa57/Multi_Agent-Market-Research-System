from crewai import Task
from datetime import datetime
from config.logging_config import logger

def create_report_writing_task(agent, context: list):
    """Create task for generating final report"""
    try:
        current_date = datetime.now().strftime("%B %Y")
        return Task(
            description=f"""Compile comprehensive report titled
                          "AI/ML Jobs in MENA - {current_date}" 
                          including visualizations and insights""",
            expected_output="Professional PDF/markdown report",
            agent=agent,
            context=context,
            output_file="output/report.md"
        )
    except Exception as e:
        logger.error(f"Failed to create report task: {str(e)}")
        raise