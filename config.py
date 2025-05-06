import os
from dotenv import load_dotenv

load_dotenv()

weather_api_key = os.getenv("weather_api_key")
database_url = os.getenv("DATABASE_URL")
