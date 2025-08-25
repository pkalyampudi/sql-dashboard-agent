from sqlalchemy import create_engine
import pandas as pd

# Example SQLite connection
engine = create_engine('sqlite:///example.db')

def run_sql_query(sql):
    with engine.connect() as conn:
        return pd.read_sql(sql, conn)

