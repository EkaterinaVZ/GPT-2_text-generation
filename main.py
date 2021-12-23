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
    return {"message": "Hello World"}

@app.post("/predict/")
def predict(item: Item):
    return generator(item.text)
