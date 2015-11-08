__author__ = 'Daniel'
from tkinter import *
from mysql.connector import MySQLConnection, Error
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = 'mysql123'
DB_NAME = 'db'

def mostrar(v):v.deiconify()
def update(v): v.update()
def query_with_fetchone(Lista1,v2):
    try:
        conn = MySQLConnection(host=DB_HOST,user=DB_USER,password=DB_PASS,database=DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT nombre FROM clientes")

        row = cursor.fetchone()
        Lista1.delete(0,END)
        while row is not None:
            d=""
            for i in row:
                if i== "("or i==")"or i=="'"or i ==",":
                    pass
                else:
                    d = d+i
            Lista1.insert(END,d)
            row = cursor.fetchone()

    except Error as e:
        print(e)

    finally:
        Lista1.grid(column=1,row=2)
        update(v2)
        cursor.close()
        conn.close()
def datos(name,v2b,nombre2,genero2,dni2,nacimiento2,domicilio2,dias2,habitacion2):
    mostrar(v2b)
    conn = MySQLConnection(host=DB_HOST,user=DB_USER,password=DB_PASS,database=DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes WHERE nombre = %s", (name,))
    user = (cursor.fetchone())
    Lrange=range(8)
    Ldatos=(nombre2,genero2,dni2,nacimiento2,domicilio2,dias2,habitacion2)
    nombre2.set(user[1])
    genero2.set(user[2])
    dni2.set(user[3])
    nacimiento2.set(user[4])
    domicilio2.set(user[5])
    dias2.set(user[6])
    habitacion2.set(user[7])
    update(v2b)
    cursor.close()
    conn.close

def dos(Lista1,v2):
    try:
        conn = MySQLConnection(host=DB_HOST,user=DB_USER,password=DB_PASS,database=DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT nombre FROM clientes")

        row = cursor.fetchone()
        Lista1.delete(0,END)
        while row is not None:
            Lista1.insert(END,row)
            row = cursor.fetchone()

    except Error as e:
        print(e)

    finally:
        update(v2)
        cursor.close()
        conn.close
