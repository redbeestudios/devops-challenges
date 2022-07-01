from sqlalchemy import Integer, Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

quotes = Table(
    "quotes",
    meta,
    Column("id", Integer, primary_key=True),
    Column("quote", String(255)),
)

meta.create_all(engine)
