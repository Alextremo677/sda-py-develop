import sqlite3
miConexion=sqlite3.connect("PruebaDB")
miCursor = miConexion.cursor()

miCursor.execute("""
    CREATE TABLE VEHICULOS (
        MATRICULA VARCHAR(10) PRIMARY KEY,
        MODELO VARCHAR(15),
        PRECIO INTEGER,
        COLOR VARCHAR(15)
        )
""")

AñadirDatos = [
    ("abc-123", "Mercedes", "5000", "gris"),
    ("def-456", "Seat", "1000", "rojo")
]

miCursor.executemany("INSERT INTO VEHICULOS VALUES (?,?,?,?)", AñadirDatos)

miConexion.commit()
miConexion.close()
