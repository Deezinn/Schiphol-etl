from sqlalchemy import create_engine, text
from src.infrastructure.security.credentials import credentials_database

def get_engine():
    """
    Função que faz conexão com o banco de dados
    """
    
    url = (
        f"postgresql+psycopg2://{credentials_database['DB_USER']}:{credentials_database['DB_PASS']}"
        f"@{credentials_database['DB_HOST']}:{credentials_database['DB_PORT']}/{credentials_database['DB_NAME']}"
    )
    return create_engine(url)
