from turtle import *
from datetime import datetime

def jump(distanz, winkel=0):
    penup()
    right(winkel)
    forward(distanz)
    left(winkel)
    pendown()

#La siguiente funcion define la forma del puntero de la flecha
def hand(laenge, spitze):
    fd(laenge*1.15)
    rt(90)
    fd(spitze/2.0)
    lt(120)
    fd(spitze)
    lt(120)
    fd(spitze)
    lt(120)
    fd(spitze/2.0)

def make_hand_shape(name, laenge, spitze):
    reset()
    jump(-laenge*0.15)
    begin_poly()
    hand(laenge, spitze)
    end_poly()
    hand_form = get_poly()
    register_shape(name, hand_form)


#Radio del reloj
def clockface(radius):
    reset()
    pensize(7) # Tamaño lineas caratula
    for i in range(60):#El valor 60 es para una vuelta de los minutis y segindos
        jump(radius)
        if i % 5 == 0:
            fd(25)
            jump(-radius-25)
        else:
            dot(3)
            jump(-radius)
        rt(6)

def setup():
    global minute_hand, hour_hand, writer
    #mode("logo")
    #Las siguientes lineas definen el tamaño de las manecillas
    #El primer dato es el largo de la manecilla y el segun es el taño de la cabeza del puntero
    make_hand_shape("minute_hand",  130, 25)
    make_hand_shape("hour_hand", 130, 25)
    clockface(160)                  #Radio del reloj

    minute_hand = Turtle()
    minute_hand.shape("minute_hand")
    minute_hand.color("blue1", "blue1")
    hour_hand = Turtle()
    hour_hand.shape("hour_hand")
    hour_hand.color("blue3", "red3")
    for hand in minute_hand, hour_hand:
        hand.resizemode("user")
        hand.shapesize(1, 1, 5) #Tamaño punta flecha, largo flecha, grosor flecha
        hand.speed(0)
    ht()
    writer = Turtle()

#La siguiente funcion define el tamaño de los pasos     
def tick():
    
    try:
        tracer(False)  # Terminator can occur here
        writer.clear()
        writer.home()
   
        #Las siguientes dos lineas defien la ubicacion del puntero 
        #El valor dentro del parentesis define el angulo de ubicacion 
        minute_hand.setheading(45)
        hour_hand.setheading(90)
        tracer(True)
        ontimer(tick, 100)
        
    except Terminator:
        pass  # turtledemo user pressed STOP

def main():
    tracer(False)
    setup()
    tracer(True)
    tick()
    
    #Las siguientes lineas definen el punto cero en X y Y de las flechas
    minute_hand.setx(-100)
    minute_hand.sety(50)
    hour_hand.setx(100)
    hour_hand.sety(50)

    return "EVENTLOOP"

if __name__ == "__main__":
    #mode("logo")
    msg = main()
    #print(msg)
    mainloop()

