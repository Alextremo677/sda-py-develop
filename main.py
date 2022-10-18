import signal
from serial import Serial
from time import sleep
from queue import Queue

from settings import Settings
from llp import LLP, data_parser
from controllers.pd import ProportionalDerivativeController
<<<<<<< Updated upstream
=======
import requests

#**************************************
import puntero
from puntero import*
#from puntero import main, tick, setup, clockface, make_hand_shape, hand, jump
#**************************************
a=0
b=0



>>>>>>> Stashed changes

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


<<<<<<< Updated upstream
sensor_map = {0xA6: "Temperature", 0x9C: "Preasure"}
=======
sensor_map = {0xA6: "Serv1", 0x9C: "Serv2"}
>>>>>>> Stashed changes
pd = ProportionalDerivativeController(kp=1, kd=0.1)

while True:
    
    if not input_queue.empty():
        values = data_parser(data=input_queue.get(), map=sensor_map)
<<<<<<< Updated upstream
=======
       
        
>>>>>>> Stashed changes
        for value in values:
            print(f"{value.name} Sensor: {value.value} with key {hex(value.key)}")
            if value.key == 0xA6:
<<<<<<< Updated upstream
                print(pd.calculate(value.value))

    sleep(0.01)
=======
                print("serv1: ",value.value)
                a=value.value
                requests.post(
                        url="http://127.0.0.1:8090/serv1",
                        json={"value": value.value}
                    )
                    
            if value.key == 0x9C:
                print("Serv2: ",value.value)
                b=value.value
                requests.post(
                        url="http://127.0.0.1:8090/serv2",
                        json={"value": value.value}
                    )

                

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
                puntero.main(a,b) #Llamo el main de puntero.py para ejecutar grafico
    sleep(0.01)
    
>>>>>>> Stashed changes
