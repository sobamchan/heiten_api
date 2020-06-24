import random
from fastapi import FastAPI


app = FastAPI()

with open('./wlist.txt') as f:
    words = [w.strip() for w in f.readlines()]


@app.get("/")
def get():
    return {"Today's heiten word is": random.sample(words, 1)[0]}
