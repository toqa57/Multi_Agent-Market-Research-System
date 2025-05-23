import os
os.environ["GOOGLE_API_KEY"] = "AIzaSyD0GP7wsqKPpvUjLP05kU7V9_qxBTYiSWc"
os.environ["GOOGLE_CSE_ID"] = "557dd79c4b2164947"



import logging
from datetime import datetime
import pandas as pd
from utils.data_manager import DataManager
from agents import WebSearchAgent, DataExtractionAgent, TrendAnalysisAgent, ReportWriterAgent
from tasks import create_web_search_task, create_data_extraction_task, create_trend_analysis_task, \
    create_report_writing_task


def configure_logging():
    """Set up comprehensive logging"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("market_research.log"),
            logging.StreamHandler()
        ]
    )
    logging.info("Logging system initialized")


def simulate_web_search():
    """Mock function to simulate web search results"""
    return [
        {
            "url": "https://linkedin.com/jobs/ai-engineer-123",
            "title": "AI Engineer",
            "company": "TechCorp",
            "skills": ["Python", "TensorFlow", "NLP"],
            "location": "Dubai",
            "date": datetime.now().strftime("%Y-%m-%d")
        },
        {
            "url": "https://bayt.com/ml-specialist-456",
            "title": "Machine Learning Specialist",
            "company": "DataSystems",
            "skills": ["Python", "PyTorch", "Computer Vision"],
            "location": "Riyadh",
            "date": datetime.now().strftime("%Y-%m-%d")
        }
    ]


def main():
    # Initialize systems
    configure_logging()
    dm = DataManager()

    # Create agents
    search_agent = WebSearchAgent().create()
    extraction_agent = DataExtractionAgent().create()
    analysis_agent = TrendAnalysisAgent().create()
    report_agent = ReportWriterAgent().create()

    # Simulate web search (replace with actual web search in production)
    logging.info("Starting web search simulation")
    search_results = simulate_web_search()
    dm.save_raw_data("linkedin", search_results, "linkedin_jobs")

    # Create and execute tasks
    search_task = create_web_search_task(search_agent)
    extraction_task = create_data_extraction_task(extraction_agent, [search_task])
    analysis_task = create_trend_analysis_task(analysis_agent, [extraction_task])
    report_task = create_report_writing_task(report_agent, [analysis_task])

    # Process results (simulated workflow)
    try:
        # Normally you would execute tasks through CrewAI here
        # For demonstration, we'll simulate the outputs

        # Simulate extracted data
        extracted_data = []
        for job in search_results:
            extracted_data.append({
                "job_title": job["title"],
                "required_skills": job["skills"],
                "location": job["location"],
                "company": job["company"]
            })

        dm.save_processed_data(extracted_data, "extracted_jobs")

        # Simulate analysis results
        analysis_results = {
            "top_titles": {
                "AI Engineer": 1,
                "Machine Learning Specialist": 1
            },
            "top_skills": {
                "Python": 2,
                "TensorFlow": 1,
                "PyTorch": 1,
                "NLP": 1,
                "Computer Vision": 1
            },
            "locations": {
                "Dubai": 1,
                "Riyadh": 1
            }
        }

        # Generate and save report
        report_path = dm.generate_report(
            analysis_results,
            "MENA_AI_Jobs_Report"
        )

        # Create visualization
        fig, ax = plt.subplots(figsize=(10, 6))
        skills = analysis_results["top_skills"]
        ax.barh(list(skills.keys()), list(skills.values()))
        ax.set_title("Most In-Demand Skills")
        dm.save_visualization(fig, "skills_distribution")

        logging.info(f"Successfully generated report at: {report_path}")

        # Show summary
        print("\n=== Market Research Summary ===")
        print(f"1. Found {len(search_results)} job postings")
        print(f"2. Top skills: {', '.join(analysis_results['top_skills'].keys())}")
        print(f"3. Report generated: {report_path}")

    except Exception as e:
        logging.error(f"Research pipeline failed: {str(e)}")
        raise


if __name__ == "__main__":
    main()