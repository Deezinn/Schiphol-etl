from dotenv import load_dotenv
import os

load_dotenv()

credentials_schiphol = {
   "accept": os.getenv("ACCEPT"),
   "app_id": os.getenv('APP_ID'),
   "app_key": os.getenv('APP_KEY'),
   "ResourceVersion": os.getenv("RESOURCE_VERSION")
}


