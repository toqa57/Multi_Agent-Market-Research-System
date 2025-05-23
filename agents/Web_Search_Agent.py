import os
import requests
from crewai import Agent, Tool
from typing import List, Dict
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('WebSearchAgent')


def search_jobs(query: str) -> List[Dict]:
    """Search for AI/ML jobs in MENA region"""
    try:
        # Using requests directly instead of SerpAPI for simplicity
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        params = {
            "q": f"{query} site:linkedin.com OR site:bayt.com OR site:wuzzuf.net",
            "location": "Dubai"
        }

        response = requests.get(
            "https://www.google.com/search",
            params=params,
            headers=headers
        )
        response.raise_for_status()

        # Note: Actual HTML parsing would be needed here
        # This is just a placeholder implementation
        return [{
            "title": f"{query} Job",
            "company": "Example Company",
            "location": "Dubai",
            "link": "https://example.com",
            "description": "Sample job description"
        }]
    except Exception as e:
        logger.error(f"Search failed: {str(e)}")
        return [{"error": str(e)}]


# Create a Tool instance manually
job_search_tool = Tool(
    name="MENAJobSearch",
    description="Searches for AI/ML jobs in MENA region",
    func=search_jobs
)


def create_web_search_agent():
    return Agent(
        role='Senior Web Research Specialist',
        goal='Find current AI/ML job postings in MENA region',
        backstory="""Expert in finding technical job postings across job boards
                  with 5+ years experience in MENA job markets.""",
        tools=[job_search_tool],
        verbose=True,
        allow_delegation=False
    )


if __name__ == "__main__":
    try:
        agent = create_web_search_agent()
        print("✅ Agent created successfully!")

        print("\nTesting search for 'AI Engineer':")
        results = search_jobs("AI Engineer")

        for i, r in enumerate(results[:3], 1):
            print(f"\nResult {i}:")
            print(f"Title: {r.get('title')}")
            print(f"Company: {r.get('company')}")
            print(f"Location: {r.get('location')}")
            print(f"Link: {r.get('link')}")
            print(f"Description: {r.get('description')}")

    except Exception as e:
        print(f"❌ Error: {str(e)}")