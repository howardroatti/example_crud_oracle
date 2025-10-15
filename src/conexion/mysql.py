# src/conexion/mysql_connection.py
import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="130595", #SUA SENHA AQ
        database="sistema_biblioteca"
    )
    return connection
