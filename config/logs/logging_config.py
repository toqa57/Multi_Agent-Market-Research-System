# config/logging_config.py
import logging
import os
from pathlib import Path
from datetime import datetime


def configure_logging():
    """Configure logging for the entire application."""

    # Create logs directory if it doesn't exist
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    # Generate timestamp for log filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = logs_dir / f"ai_ml_jobs_mena_{timestamp}.log"

    # Basic configuration
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_filename),  # Save to file
            logging.StreamHandler()  # Print to console
        ]
    )

    # Special configuration for specific modules
    library_loggers = [
        'crewai',
        'langchain',
        'urllib3'
    ]

    for logger_name in library_loggers:
        logging.getLogger(logger_name).setLevel(logging.WARNING)

    # Add our own logger
    logger = logging.getLogger("ai_ml_jobs_mena")
    logger.info("Logging system initialized")

    return logger


# Initialize logging when this module is imported
logger = configure_logging()