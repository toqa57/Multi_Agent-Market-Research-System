from crewai import Agent
from langchain_community.tools import DuckDuckGoSearchRun
from config.logging_config import logger


class DataExtractionAgent:
    def __init__(self):
        self.tools = self._setup_tools()

    def _setup_tools(self):
        """Setup tools for data extraction"""
        return [
            DuckDuckGoSearchRun(),  # For general web searches
            # Add other scraping tools as needed
        ]

    def create(self):
        return Agent(
            role='Data Extraction Specialist',
            goal='Extract structured job details from postings',
            backstory="""Skilled in parsing HTML and extracting job titles, 
                      skills, locations from complex job postings.""",
            verbose=True,
            tools=self.tools,
            allow_delegation=False,
            memory=True
        )