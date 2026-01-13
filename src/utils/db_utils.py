import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

def get_engine(echo: bool = False):
    import os
    from dotenv import load_dotenv

    load_dotenv()

    user = os.getenv("user")
    password = os.getenv("password")
    host = os.getenv("host")
    port = os.getenv("port")
    dbname = os.getenv("dbname")

    database_url = f"postgresql+psycopg://{user}:{password}@{host}:{port}/{dbname}?sslmode=require"

    return create_engine(
        database_url,
        echo=True,
        pool_size=10,          # increase max connections
        max_overflow=5,        # allow temporary extra connections
        pool_timeout=60,       # wait 30s for connection before error
    )


def insert_dataframe(
        df: pd.DataFrame,
        table_name: str,
        engine: Engine,
        schema: str = "public",
    ):
    """
    Insert a pandas DataFrame into a PostgreSQL table.
    """
    if df.empty:
        return

    # Insert in chunks to avoid pool timeout
    df.to_sql(
        name=table_name,
        con=engine,
        schema=schema,
        if_exists="append",
        index=False,
        method="multi",
        chunksize=500
    )

    engine.dispose() # close connections after done