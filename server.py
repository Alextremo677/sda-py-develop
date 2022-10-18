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

servo1 = []
servo2 = []

class Serv1(BaseModel):
    value: int

class Serv2(BaseModel):
    value: int
"""
@app.get("/")
def read_root():
    return {"Hello": "World", "UTC": datetime.utcnow()}
"""


@app.post("/serv1")
def pid_serv1(serv1: Serv1):
    response = {"value": serv1.value, "time": datetime.utcnow()}
    servo1.append(response)
    return response
    #return {"Hello222": "World", "UTC": datetime.utcnow()}

@app.get("/serv1")
def get_serv1():
    return servo1.pop(0) if len(servo1) > 0 else []
    #return {"Hello": "World", "UTC": datetime.utcnow()}



"""
@app.post("/serv1")
#def pid_serv1(serv1: Serv1, serv2: Serv2):
def pid_serv1(serv1: Serv1):
    response = {"value": serv1.value, "value2": serv1.value}
    servo1.append(response)
    #servo2.append(response)
    return response
    #return {"Hello222": "World", "UTC": datetime.utcnow()}

@app.get("/serv1")
def get_serv1():
    return servo1.pop(0) if len(servo1) > 0 else []
    #return {"Hello": "World", "UTC": datetime.utcnow()}

"""



#---------------------------------------------------------------------------------
@app.post("/serv2")
def pid_serv2(serv2: Serv2):
    response = {"value": serv2.value, "time": datetime.utcnow()}
    servo2.append(response)
    return response
    #return {"Hello222": "World", "UTC": datetime.utcnow()}

@app.get("/serv2")
def get_serv2():
    return servo2.pop(0) if len(servo2) > 0 else []
    #return {"Hello": "World", "UTC": datetime.utcnow()}

#-----------------------------------------------------------------------------------


if __name__ == "__main__":
    uvicorn.run(
        app, host="127.0.0.1", port=8090, workers=1, log_level="debug"
    )