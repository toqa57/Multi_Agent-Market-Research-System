# Multi-Agent Market Research System Setup Guide


🚀 Quick Start
Prerequisites
Python 3.8+ installed
API keys for OpenAI and Serper
1. Environment Setup
bash
# Create virtual environment
python -m venv mena_job_analysis
source mena_job_analysis/bin/activate  # On Windows: mena_job_analysis\Scripts\activate

# Install dependencies
pip install -r requirements.txt
2. API Keys Configuration
Create a .env file in your project root:

env
# OpenAI API Key (required for LLM)
OPENAI_API_KEY=your_openai_api_key_here

# Serper API Key (required for web search)
SERPER_API_KEY=your_serper_api_key_here

# Optional: Other API keys
LINKEDIN_API_KEY=your_linkedin_api_key
GLASSDOOR_API_KEY=your_glassdoor_api_key
3. Get Your API Keys
OpenAI API Key
Go to OpenAI Platform
Create account or log in
Generate new API key
Copy and paste into .env file
Serper API Key (Free tier available)
Go to Serper.dev
Sign up for free account
Get your API key from dashboard
Copy and paste into .env file
4. Project Structure
Create the following directory structure:

mena_job_analysis/
├── main.py                 # Main application file
├── requirements.txt        # Dependencies
├── .env                   # Environment variables (create this)
├── config/
│   ├── __init__.py
│   └── settings.py        # Configuration settings
├── agents/
│   ├── __init__.py
│   ├── web_search_agent.py
│   ├── data_extraction_agent.py
│   ├── trend_analysis_agent.py
│   └── report_writer_agent.py
├── tools/
│   ├── __init__.py
│   ├── job_scrapers.py
│   └── data_processors.py
├── data/
│   ├── raw/               # Raw scraped data
│   ├── processed/         # Cleaned data
│   └── reports/           # Generated reports
└── utils/
    ├── __init__.py
    ├── visualizations.py
    └── helpers.py
5. Run the Analysis
bash
# Make sure you're in the virtual environment
source mena_job_analysis/bin/activate

# Run the main analysis
python main.py
🔧 Advanced Configuration
Custom Settings
Create config/settings.py:

python
# Target Countries
MENA_COUNTRIES = [
    'United Arab Emirates', 'Saudi Arabia', 'Egypt', 
    'Qatar', 'Jordan', 'Morocco', 'Tunisia', 'Lebanon'
]

# Job Search Keywords
AI_ML_KEYWORDS = [
    'Machine Learning Engineer', 'Data Scientist', 'AI Engineer',
    'Deep Learning Engineer', 'MLOps Engineer', 'Computer Vision Engineer',
    'NLP Engineer', 'AI Researcher', 'Data Engineer', 'ML Researcher'
]

# Job Platforms to Search
JOB_PLATFORMS = [
    'linkedin.com', 'bayt.com', 'wuzzuf.net', 
    'glassdoor.com', 'indeed.com'
]

# Analysis Parameters
MIN_JOB_POSTINGS = 200
ANALYSIS_DEPTH = 'comprehensive'  # 'basic', 'standard', 'comprehensive'
INCLUDE_SALARY_DATA = True
GENERATE_VISUALIZATIONS = True
Custom Agent Configurations
You can modify agent behaviors in the main script or create separate agent files for more complex configurations.

📊 Expected Outputs
After running the analysis, you'll get:

Main Report: ai_ml_jobs_mena_report.md
Data Files: Raw and processed data in data/ folder
Visualizations: Charts and graphs in PNG format
Log Files: Detailed execution logs
🛠️ Troubleshooting
Common Issues
API Key Errors
Error: OpenAI API key not found
Check your .env file exists and has correct API keys
Ensure no spaces around the = sign in .env
Rate Limiting
Error: Rate limit exceeded
The script includes rate limiting - wait and retry
Consider upgrading API plans for higher limits
Web Scraping Blocks
Error: Access denied or blocked
Some sites block automated scraping
The system will skip blocked sources and continue
Memory Issues
Error: Out of memory
Reduce MIN_JOB_POSTINGS in settings
Process data in smaller batches
Performance Optimization
Faster Execution: Reduce the number of job postings to analyze
Better Quality: Increase the analysis depth in settings
Cost Control: Monitor API usage through provider dashboards
🔍 Customization Options
Add New Job Platforms
Modify the web search agent to include additional platforms:

python
# In the search task description, add:
"- Monster Gulf"
"- Naukrigulf"  
"- Dubizzle Jobs"
Custom Analysis Metrics
Add new analysis dimensions in the trend analysis task:

python
"6. Company Analysis:"
"   - Top hiring companies"
"   - Startup vs Enterprise preferences"
"   - Company size distribution"
Different Output Formats
Modify the report writer agent to generate:

PDF reports
Interactive dashboards
Excel spreadsheets
PowerPoint presentations
📈 Sample Results Preview
The system will generate insights like:

Top Role: Data Scientist (35% of postings)
Hot Skill: Python (mentioned in 78% of jobs)
Growing Market: UAE leads with 40% of opportunities
Salary Range: $60K-120K for senior ML engineers
Remote Work: 25% of positions offer remote options
🤝 Support and Contributions
For issues or improvements:

Check the troubleshooting section
Review API documentation
Adjust configurations as needed
The system is designed to be flexible and expandable for different regions and job markets.

