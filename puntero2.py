import tkinter as tk
import math 
my_w = tk.Tk()
width,height=410,310 # set the variables 
d=str(width)+"x"+str(height+40)
my_w.geometry(d) 
c1 = tk.Canvas(my_w, width=width-10, height=height-50,bg='#FFFFFF')
c1.grid(row=0,column=0)
arc_w=50 # width of the arc 
x1,y1,x2,y2=35,35,355,355 # dimensions for the arc 
x,y,r=195,195,135


#Define colores para el arco
c1.create_arc(x1, y1,x2,y2, start=0, extent=45,outline='green',
         width=arc_w,style=tk.ARC)
c1.create_arc(x1, y1,x2,y2, start=45, extent=45,outline='blue', 
        width=arc_w,style=tk.ARC)
c1.create_arc(x1, y1,x2,y2, start=90, extent=30,outline='yellow', 
        width=arc_w,style=tk.ARC)
c1.create_arc(x1, y1,x2,y2, start=120, extent=60,outline='red',
        width=arc_w,style=tk.ARC)
        
# Cirxulo central
c1.create_oval(x-10,y-10,x+10,y+10,fill='blue') 
in_radian=math.radians(0) # getting radian value 
line=c1.create_line(x,y,(x+r*math.cos(in_radian)),
        (y-r*math.sin(in_radian)),width=6,arrow='last')

def my_upd(value):
    global line
    in_radian = math.radians(my_scale.get()) # scale value in radian
    c1.delete(line) # Borra la linea
    line=c1.create_line(x,y,(x+r*math.cos(in_radian)),
            (y-r*math.sin(in_radian)),width=6,arrow='last')#Crea la nueva linea

my_scale = tk.Scale(my_w, from_=0, to=180, orient='horizontal',
    length=300,command= my_upd)
my_scale.grid(row=2,column=0) 
my_w.mainloop()