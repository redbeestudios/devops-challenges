from fastapi import FastAPI
from routes.quote import quote 

app = FastAPI(
    title="Simpsons Quotes API",
    description="The Simpsons quotes API for your pleasure",
    openapi_tags=[{
        "name": "quotes",
        "description": "simpsons quotes endpoints"
    }]
)
app.include_router(quote)

