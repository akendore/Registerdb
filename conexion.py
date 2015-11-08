__author__ = 'Daniel'
from datetime import date
from mysql.connector import MySQLConnection, Error
import ventana2
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = 'mysql123'
DB_NAME = 'db'

def insert_client(nombre,genero,dni,nacimiento,residencia,dias,habitacion,v):
    query = ("INSERT INTO clientes "
                "(nombre,genero,dni,nacimiento,residencia,dias,habitacion)"
                "VALUES (%s,%s,%s,%s,%s,%s,%s)")
    args = (nombre,genero,dni,nacimiento,residencia,dias,habitacion)

    try:
        conn = MySQLConnection(host=DB_HOST,user=DB_USER,password=DB_PASS,database=DB_NAME)
        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
        v.update()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()
