from crewai import Agent
from config.logging_config import logger

class TrendAnalysisAgent:
    def create(self):
        return Agent(
            role='Market Trend Analyst',
            goal='Identify patterns in AI/ML job market',
            backstory="""Data scientist specializing in labor market analytics
                      with expertise in MENA region tech trends.""",
            verbose=True,
            tools=[],  # Uses LLM analysis capabilities
            allow_delegation=False
        )