from crewai import Agent
from tools import custom_tools  # Import from tools package
from config.logging_config import logger

class ReportWriterAgent:
    def __init__(self):
        try:
            # Get all tools using the factory function
            self.tools = custom_tools()
            logger.info("Successfully loaded custom tools")
        except Exception as e:
            logger.error(f"Failed to initialize tools: {str(e)}")
            self.tools = []

    def create(self) -> Agent:
        """Create and configure the agent instance"""
        return Agent(
            role='Senior Business Analyst',
            goal='Create professional market reports',
            backstory="""Experienced in transforming raw data into polished
                      business reports with actionable insights.""",
            verbose=True,
            tools=self.tools,
            allow_delegation=False,
            memory=True  # Recommended for report writing agents
        )