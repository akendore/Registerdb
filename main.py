__author__ = 'Daniel'
from datetime import date
from tkinter import *
import conexion
import ventana2
import eliminar
title = "title" #Nombre de la ventana
def mostrar(v):v.deiconify()
def ocultar(v):v.withdraw()
def ejecutar(f):v0.after(200,f)
def guardar(n,g,dni,f,r,d,h):
    no = n.get()
    ge = g.get()
    DnI = dni.get()
    fe = f
    res = r.get()
    di = d.get()
    ha = h.get()
    conexion.insert_client(no,ge,DnI,fe,res,di,ha,v2)
    ocultar(v1)
    n.set("")
    g.set("")
    dni.set("")
    r.set("")
    d.set("")
    h.set("")
#Configuración de la ventana
v0 = Tk()
v0.title(title)
F0 = Frame(v0)
F0.grid(column=0,row=0,padx=10,pady=10)
v0.resizable(0,0)

#Ventana registro
v1 = Toplevel(v0)
v1.withdraw()
v1.title = "Registrar nuevo usuario"
F1 = Frame(v1)
F1.grid(column=0,row=0,padx=10,pady=10)
v1.resizable(0,0)
#Ventana ver
v2 = Toplevel(v0)
v2.withdraw()
v2.title = "Ver clientes registrados"
F2 = Frame(v2)
F2.grid(column=0,row=0,padx=10,pady=10)
v2.resizable(0,0)
#Ventana ver2
v2b = Toplevel(v0)
v2b.withdraw()
v2b.resizable(0,0)
v2b.title = "Ver cliente "
F2b = Frame(v2b)
F2b.grid(column=0,row=0,padx=10,pady=10)

#Elementos v0
    #BOTONES
B1 = Button(F0,text="Registrar cliente",command=lambda:ejecutar(mostrar(v1))).grid(column=1,row=1,padx=5,pady=5)
B2 = Button(F0,text="Ver clientes registrados",command=lambda:ejecutar(mostrar(v2))).grid(column=2,row=1,padx=5,pady=5)

#Elementos v1
    #Labels
L1v1 = Label(F1,text="Nombre:").grid(column=1,row=1)
L2v2 = Label(F1,text="Género:").grid(column=1,row=2)
L3v1 = Label(F1,text="DNI:").grid(column=1,row=3)
L4v1 = Label(F1,text="Fecha de nacimiento:").grid(column=1,row=4)
L5v1 = Label(F1,text="Domicilio:").grid(column=1,row=5)
L6v1 = Label(F1,text="Días previstos:").grid(column=1,row=6)
L7v1 = Label(F1,text="Habitación:").grid(column=1,row=7)

    #Entradas
Nombre = StringVar()
E1v1 = Entry(F1,textvar=Nombre).grid(column=2,row=1)
DNI = StringVar()
E3v1 = Entry(F1,textvar=DNI).grid(column=2,row=3)
Residencia = StringVar()
E5v1 = Entry(F1,textvar=Residencia).grid(column=2,row=5)
Habitacion = StringVar()
E7v1 = Entry(F1,textvar=Habitacion).grid(column=2,row=7,columnspan=2)

    #Radio Butons
v = StringVar()

Radiobutton(F1, text="M", variable=v, value="M").grid(column=2,row=2)
Radiobutton(F1, text="F", variable=v, value="F").grid(column=3,row=2)

    #Choose
optionList1 = []
for i in range(1,31):
    optionList1.append(i)
Dias = IntVar()
OptionMenu(F1, Dias, *optionList1).grid(column=2,row=6)

optionList2 = []
for i in range(1,32):
    optionList2.append(i)
nDia = IntVar()
OptionMenu(F1, nDia, *optionList2).grid(column=2,row=4)

optionList3 = []
for i in range(1,13):
    optionList3.append(i)
nMes = StringVar()
OptionMenu(F1, nMes, *optionList3).grid(column=3,row=4)

optionList4 = []
for i in range(1935,2016):
    optionList4.append(i)
nAño = IntVar()
OptionMenu(F1, nAño, *optionList4).grid(column=4,row=4)

    #Botones
b1v1 = Button(F1,text="Guardar",command=lambda:ejecutar(guardar(Nombre,v,DNI,date(int(nAño.get()),int(nMes.get()),int(nDia.get())),Residencia,Dias,Habitacion)or (ventana2.query_with_fetchone(Lista1,v2)))).grid(column=2,row=8)
b2v1 = Button(F1,text="Cerrar",command=lambda:ejecutar(ocultar(v1))).grid(column=3,row=8)


#Elementos v2
    #Listas
#Configuración de la 2ª Ventana
#nombre,genero,dni,nacimiento,residencia,dias,habitacion
Lnombre1 = Label(F2b,text="Nombre:").grid(column=1,row=1)
Lgenero1 = Label(F2b,text="Género:").grid(column=1,row=2)
Ldni1 = Label(F2b,text="DNI:").grid(column=1,row=3)
Lnacimiento1 = Label(F2b,text="Nacimiento:").grid(column=1,row=4)
Ldomicilio1 = Label(F2b,text="Domicilio:").grid(column=1,row=5)
Ldias1 = Label(F2b,text="Dias:").grid(column=1,row=6)
Lhabitacion1 = Label(F2b,text="Habitación").grid(column=1,row=7)

#Etiquetas variables

nombre2 = StringVar()
genero2 = StringVar()
dni2 = StringVar()
nacimiento2 = StringVar()
domicilio2 = StringVar()
dias2 = StringVar()
habitacion2 = StringVar()

Lnombre2 = Label(F2b,textvar=nombre2).grid(column=2,row=1)
Lgenero2 = Label(F2b,textvar=genero2).grid(column=2,row=2)
Ldni2 = Label(F2b,textvar=dni2).grid(column=2,row=3)
Lnacimiento2 = Label(F2b,textvar=nacimiento2).grid(column=2,row=4)
Ldomicilio2 = Label(F2b,textvar=domicilio2).grid(column=2,row=5)
Ldias2 = Label(F2b,textvar=dias2).grid(column=2,row=6)
Lhabitacion2 = Label(F2b,textvar=habitacion2).grid(column=2,row=7)
B1b = Button(F2b,text="Cerrar",command=lambda:ejecutar(ocultar(v2b))).grid(column=1,row=8)
B2 = Button(F2b,text="Dar de baja",command=lambda:ejecutar(eliminar.dardebaja(nombre2,dias2))or(ventana2.query_with_fetchone(Lista1,v2))or(ocultar(v2b))).grid(column=2,row=8)
Lenv2 = Label(F2,text="Haz doble clic en un cliente para ver su información:").grid(column=1,row=1)
Lista1 = Listbox(F2)
B1a = Button(F2,text="Cerrar",command=lambda:ejecutar(ocultar(v2))).grid(column=2,row=3)
ventana2.query_with_fetchone(Lista1,v2)

Lista1.bind('<Double-1>', lambda x: ventana2.datos(Lista1.selection_get(),v2b,nombre2,genero2,dni2,nacimiento2,domicilio2,dias2,habitacion2))
v0.mainloop()
