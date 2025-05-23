from crewai import Agent
from langchain_community.tools import DuckDuckGoSearchRun
from config.logging_config import logger
from typing import List, Dict
import os
import requests
from crewai import Tool
import logging

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

class ReportWriterAgent:
    def __init__(self):
        try:
            # Get all tools using the factory function
            from tools import custom_tools
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

class WebSearchAgent:
    def __init__(self):
        self.tools = [self._create_search_tool()]

    def _create_search_tool(self):
        """Create the job search tool"""
        return Tool(
            name="MENAJobSearch",
            description="Searches for AI/ML jobs on LinkedIn, Bayt, and Wuzzuf in MENA region",
            func=self._search_jobs
        )

    def _search_jobs(self, query: str) -> List[Dict]:
        """Search for AI/ML jobs in MENA region using SerpAPI"""
        try:
            api_key = os.getenv("SERPAPI_KEY", "your_api_key_here")
            params = {
                "q": f"{query} site:linkedin.com OR site:bayt.com OR site:wuzzuf.net",
                "location": "Dubai,United Arab Emirates",
                "hl": "en",
                "gl": "ae",
                "api_key": api_key,
                "num": 5
            }

            response = requests.get("https://serpapi.com/search", params=params)
            results = response.json().get("organic_results", [])

            formatted_results = []
            for r in results:
                title = r.get("title", "")
                company = title.split(" at ")[1].split(" in ")[0].strip() if " at " in title else r.get("source", "Unknown")
                formatted_results.append({
                    "title": title,
                    "company": company,
                    "link": r.get("link", "#"),
                    "description": r.get("snippet", "")[:200] + "..." if r.get("snippet") else ""
                })
            return formatted_results
        except Exception as e:
            logger.error(f"Search failed: {str(e)}")
            return [{"error": "Search service unavailable"}]

    def create(self):
        return Agent(
            role='Senior Web Research Specialist',
            goal='Find current AI/ML job postings in MENA region',
            backstory="""Expert in finding technical job postings across LinkedIn, Bayt, and Wuzzuf
                      with 5+ years experience in MENA job markets.""",
            tools=self.tools,
            verbose=True,
            allow_delegation=False
        )

__all__ = ['DataExtractionAgent', 'ReportWriterAgent', 'TrendAnalysisAgent', 'WebSearchAgent']