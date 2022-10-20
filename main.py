import signal
from urllib import response
from serial import Serial
from time import sleep
from queue import Queue

from settings import Settings
from llp import LLP, data_parser
from controllers.pd import ProportionalDerivativeController

from dis import Instruction
import sqlite3 as sql

from sql import createDB, createTable, deleteTable, insertRow, insertRows, readRow, deleteTable, search, get_last
#**************************************
import puntero
#from puntero import main, tick, setup, clockface, make_hand_shape, hand, jump
#**************************************


import requests

a= "Servo 1"
b = "Servo 2"
c = 0
d = 0


settings = Settings()

input_queue = Queue(maxsize=10)

llp = LLP(
    port=settings.PORT,
    baudrate=settings.BAUDRATE,
    timeout=0.1,
    header=0x7E,
    queue=input_queue,
)

def handler(signum, frame):
    print("\nCtrl-c was pressed.")
    llp.stop()
    exit()

signal.signal(signal.SIGINT, handler)

llp.start()

sensor_map = {0xA6: "Serv1", 0x9C: "Serv2"}
pd = ProportionalDerivativeController(kp=1, kd=0.1)


deleteTable()
while True:
    if not input_queue.empty():
        values = data_parser(data=input_queue.get(), map=sensor_map)
        
        for value in values:
            #print(f"{value.name} Sensor: {value.value} with key {hex(value.key)}")
            if value.key == 0xA6:
                #print("serv1: ",value.value)
                c=value.value
                requests.post(
                        url="http://127.0.0.1:8090/serv1",
                        json={"value": value.value}
                    )
                    
            if value.key == 0x9C:
                #print("Serv2: ",value.value)
                d=value.value
                requests.post(
                        url="http://127.0.0.1:8090/serv2",
                        json={"value": value.value}
                    )


                #puntero.main(a,b)


                DBservos = [(a , c, b , d)]
                insertRows(DBservos)
                #readRow()



                #search()
                print(get_last()[1])

                
                """
                respons = requests.get("http://127.0.0.1:8000")
                print(respons)
                
                
                try:
                    requests.post(
                        url="http://127.0.0.1:8080/temperature",
                        json={"value": value.value}
                    )
                except Exception as e:
                    print(e)
                print(value)
                """
    sleep(0.01)