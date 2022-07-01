from sqlalchemy import create_engine, MetaData
import os

db_host = os.getenv("DB_HOST", "localhost")
db_port = os.getenv("DB_PORT", "3306")
db_user = os.getenv("DB_USER", "appuser")
db_password = os.getenv("DB_PASS", "Password123*")

engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/simpsons_quotes")

meta = MetaData()

conn = engine.connect()