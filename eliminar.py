from tkinter import *
from mysql.connector import MySQLConnection, Error
from tkinter.messagebox import *
import ventana2
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = 'mysql123'
DB_NAME = 'db'
valorxnoche = 30
def ocultar(v):v.withdraw()
def dardebaja(nombre,dias):
    _dias = int(dias.get())
    _nombre = nombre.get()
    preciofinal = _dias*valorxnoche
    showinfo("Precio final","El precio final será de: %s€)" % preciofinal)
    try:
        conn = MySQLConnection(host=DB_HOST,user=DB_USER,password=DB_PASS,database=DB_NAME)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clientes WHERE nombre=%s",(_nombre,))
        conn.commit()
        #v.update()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
        #ocultar(v2b)
