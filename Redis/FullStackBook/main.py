import json

import requests
import redis
from fastapi import FastAPI

rd = redis.Redis(host='localhost', port=6379, db=0)

app = FastAPI()


@app.get("/")
def read_root():
    return "Hello World!"


@app.get("/agify/{name}")
def read_fish(name: str):

    cache = rd.get(name)
    if cache:
        print("cache hit")
        return json.loads(cache)
    print("cache miss")
    response = requests.get(f"https://api.agify.io?name={name}")
    rd.set(name, response.text)
    rd.expire(name, 5)
    return response.json()
