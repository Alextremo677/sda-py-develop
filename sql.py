from dis import Instruction
import sqlite3 as sql

a= "Servo 1"
b = "Servo 2"
c = 1.4
d = 1

def createDB():
    conn = sql.connect("DBservos.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("DBservos.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE DBservos (
            Motor1 text,
            Angulo1 integer,
            Motor2 text,
            Angulo2 integer
        )"""
    )
    conn.commit()
    conn.close()

def insertRow(Motor1, Angulo1, Motor2, Angulo2):

        conn = sql.connect("DBservos.db")
        cursor = conn.cursor()
        instruccion = f"INSERT INTO DBservos VALUES('{Motor1}',{Angulo1},'{Motor2}',{Angulo2})"
        cursor.execute(instruccion)
        conn.commit()
        conn.close()

def insertRows(DBservosList):
    conn = sql.connect("DBservos.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO DBservos VALUES(?, ?, ?, ?)"
    cursor.executemany(instruccion, DBservosList)
    conn.commit()
    conn.close()

def readRow():
    conn = sql.connect("DBservos.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM DBservos"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)



def deleteTable():
    conn = sql.connect("DBservos.db")
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM DBservos"
    )
    conn.commit()
    conn.close()

def search():
    conn = sql.connect("DBservos.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM DBservos WHERE Angulo1 like 0" #filtrar con el where
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)


def get_last():
    conn = sql.connect("DBservos.db")
    cursor = conn.cursor()
    res = cursor.execute('SELECT * FROM DBservos')
    return res.fetchall()[-1]


if __name__ == "__main__":
    deleteTable()
    #createDB()
    #createTable()
    DBservos = [
        (a , c, b , d)
    ]
    insertRows(DBservos)
    readRow()