import uvicorn
from typing import Union

import socket
import http.server

from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel

from settings import Settings
from controllers.pd import ProportionalDerivativeController


app = FastAPI()
settings = Settings()

temperatures = []

class Temperature(BaseModel):
    value: int

@app.get("/")
def read_root():
    return {"Hello": "World", "UTC": datetime.utcnow()}

@app.post("/temperature")
def pid_temperature(temperature: Temperature):
    response = {"value": temperature.value, "time": datetime.utcnow()}
    temperatures.append(response)
    return response
    #return {"Hello222": "World", "UTC": datetime.utcnow()}

@app.get("/temperature")
def get_temperature():
    #return temperatures.pop(0) if len(temperatures) > 0 else []
    return {"Hello": "World", "UTC": datetime.utcnow()}

if __name__ == "__main__":
    uvicorn.run(
        app, host="127.0.0.1", port=7800, workers=1, log_level="debug"
    )