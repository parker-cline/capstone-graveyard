import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Set Flask configuration vars from .env file."""

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]