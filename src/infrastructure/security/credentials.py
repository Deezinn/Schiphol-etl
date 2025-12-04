from dotenv import load_dotenv
import os

load_dotenv()

credentials_schiphol = {
   "accept": os.getenv("ACCEPT"),
   "app_id": os.getenv('APP_ID'),
   "app_key": os.getenv('APP_KEY'),
   "ResourceVersion": os.getenv("RESOURCE_VERSION")
}

credentials_database = {
    "DB_USER": os.getenv("DB_USER"), 
    "DB_PASS": os.getenv("DB_PASS"), 
    "DB_HOST": os.getenv("DB_HOST"), 
    "DB_PORT": os.getenv("DB_PORT"), 
    "DB_NAME": os.getenv("DB_NAME"), 
}