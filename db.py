#Comandos usados para instalar la libreria mySQL
#pip install PyMySQL
#pip install mysql-connector-python



# Importing module 
import mysql.connector
  
# Creating connection object
mydb = mysql.connector.connect(
    host = "localhost",
    user = "yourusername",
    password = "your_password"
)
  
# Printing the connection object 
print(mydb)