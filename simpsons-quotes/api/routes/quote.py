from fastapi import APIRouter, Response
from config.db import conn
from models.quote import quotes
from schemas.quote import Quote
from starlette import status

quote = APIRouter()


@quote.get("/quotes", response_model=list[Quote], tags=["quotes"])
def get_quotes():
    return conn.execute(quotes.select()).fetchall()


@quote.post("/quotes", response_model=Quote, tags=["quotes"])
def create_quote(quote: Quote):
    new_quote = {"quote": quote.quote}
    result = conn.execute(quotes.insert().values(new_quote))
    print(result.lastrowid)
    return conn.execute(quotes.select().where(quotes.c.id == result.lastrowid)).first()


@quote.get("/quotes/{id}", response_model=Quote, tags=["quotes"])
def get_quote(id: str):
    return conn.execute(quotes.select().where(quotes.c.id == id)).first()


# @quote.delete("/quotes/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_quote(id: str):
#     conn.execute(quotes.delete().where(quotes.c.id == id))
#     return Response(status_code=status.HTTP_204_NO_CONTENT)
