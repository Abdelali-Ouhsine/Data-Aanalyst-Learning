import pandas as pd
from sqlalchemy import create_engine, text
import dotenv
from urllib.parse import quote_plus
import os
dotenv.load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

url = (
    f"postgresql+psycopg2://{DB_USER}:"
    f"{quote_plus(DB_PASSWORD)}@"
    f"{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(url)

with engine.connect() as con:
    con.execute(text("SELECT version();"))

df = pd.read_csv("./london_road.csv")

df.to_sql(
    "bikes_london",
    engine,
    if_exists="replace",
    index=False
)