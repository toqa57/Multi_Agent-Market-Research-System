import os


class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")

    # Job platforms to search
    JOB_PLATFORMS = [
        "linkedin.com",
        "bayt.com",
        "wuzzuf.net",
        "glassdoor.com",
        "gulftalent.com",
        "naukrigulf.com"
    ]

    # MENA countries list
    MENA_COUNTRIES = [
        "UAE", "Saudi Arabia", "Qatar", "Kuwait",
        "Oman", "Bahrain", "Egypt", "Morocco",
        "Algeria", "Tunisia", "Jordan", "Lebanon"
    ]


settings = Settings()