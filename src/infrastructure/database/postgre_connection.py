from sqlalchemy import create_engine
from ..security import credentials_database

url = (
    f"postgresql+psycopg2://{credentials_database['DB_USER']}:{credentials_database['DB_PASS']}"
    f"@{credentials_database['DB_HOST']}:{credentials_database['DB_PORT']}/{credentials_database['DB_NAME']}"
)

engine = create_engine(url)
conn = engine.connect()
print('conectou', conn)