import os

from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "DocIQ")
    APP_ENV: str = os.getenv("APP_ENV", "development")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")
    LLM_API_KEY: str = os.getenv("LLM_API_KEY", "")

    def validate(self) -> None:
        if not self.APP_NAME:
            raise ValueError("APP_NAME is not configured.")

        if self.APP_ENV not in {"development", "testing", "production"}:
            raise ValueError(
                "APP_ENV must be development, testing, or production."
            )
        
settings = Settings()
settings.validate()