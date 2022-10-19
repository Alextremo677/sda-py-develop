from dis import Instruction
import sqlite3 as sql 

def createDB():
    conn = sql.connect("streamers.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE streamers (
            Motor text,
            Angulo integer
        )"""
    )
    conn.commit()
    conn.close()

def insertRow(Motor, Angulo):

        conn = sql.connect("streamers.db")
        cursor = conn.cursor()
        instruccion = f"INSERT INTO streamers VALUES('{Motor}',{Angulo})"
        cursor.execute(instruccion)
        conn.commit()
        conn.close()

def readRow():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def insertRows(streamersList):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO streamers VALUES(?, ?)"
    cursor.executemany(instruccion, streamersList)
    conn.commit()
    conn.close()

def readOrdered(field):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers ORDER BY {field}"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)


if __name__=="main_":
    createDB()
    createTable()
    #insertRow("servo 1", 45)
    #insertRow("servo 2", 80)
    #insertRow("servo 1", 15)
    #insertRow("servo 2", 130)
    #readRow()
    streamers = [
        ("servo1","67"),
        ("servo2","56"),
        ("servo1","45"),
        ("servo2","12"),
        ("servo1","43"),
        ("servo2","78"),
        ("servo1","0")
    ]
    #insertRows(streamers)
    readOrdered("angulo")