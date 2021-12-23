# https://huggingface.co/gpt2
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline, set_seed

generator = pipeline('text-generation', model='gpt2')
set_seed(42)


class Item(BaseModel):
    text: str


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World!"}


@app.post("/predict/")
def predict(item: Item):
    """ Text = text in English.
    Examples: I have to go to the university., There is the house where my family lives., We go jogging every Sunday."""
    return generator(item.text)
# uvicorn text_generation:app
# env\Scripts\activate.bat

