from sqlalchemy import create_engine
from ..security import credentials_database

DATABASE_URL = f"postgresql+psycopg2://{credentials_database['DB_USER']}:{credentials_database["DB_PASS"]}@{credentials_database["DB_HOST"]}:{credentials_database['DB_PORT']}/{credentials_database['DB_NAME']}"

engine = create_engine(DATABASE_URL)
conn = engine.connect()
