

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# denfine endpoint
@app.get("/")
async def root():
    return {
        "message": "Hello World!"
    }


# End point with request
class Items(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/items/")
async def create_item( item: Items ):
    return item



















