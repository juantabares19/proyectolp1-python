from tkinter import *
from tkinter import ttk
import pandas as pd
#pip install pandastable, python3 -m pip install pandastable
from pandastable import Table, TableModel

#listas globales
idp,nombre_producto,unidades,costo,empresa=[],[],[],[],[]

def agregar_datos():
    global idp,nombre_producto,unidades,costo,empresa
    idp.append(txtidp.get())
    nombre_producto.append(txtnombre_producto.get())
    unidades.append(txtunidades.get())
    costo.append(txtcosto.get())
    empresa.append(txtempresa.get())
    limpiar()

def limpiar():
    txtidp.delete(0,END)
    txtnombre_producto.delete(0,END)
    txtunidades.delete(0,END)
    txtcosto.delete(0,END)
    txtempresa.delete(0,END)

def mostrar_datos():
    tabla.delete(*tabla.get_children())
    global idp,nombre_producto,unidades,costo,empresa  
    for i in range(len(idp)):
        tabla.insert('',END,text=idp[i], values=(nombre_producto[i],unidades[i],costo[i],empresa[i]))
    
ventana= Tk()
ventana.title('Guardar datos en excel')
ventana.geometry('800x600')
ventana.resizable(1,1)

frame1= Frame(ventana,bg='gray15')
frame1.grid(row=0,column=0,sticky='nsew')

frame2= Frame(ventana,bg='gray16')
frame2.grid(row=0,column=1,sticky='nsew')

lblidp= Label(frame1, text='Nombre', width=10)
lblidp.grid(row=0,column=0,padx=10, pady=20)
txtidp=Entry(frame1, width=20, font=('Arial',12))
txtidp.grid(row=0,column=1)

lblnombre_producto= Label(frame1, text='Apellido', width=10)
lblnombre_producto.grid(row=1,column=0,padx=10, pady=20)
txtnombre_producto=Entry(frame1, width=20, font=('Arial',12))
txtnombre_producto.grid(row=1,column=1)

lblunidades= Label(frame1, text='Edad', width=10)
lblunidades.grid(row=2,column=0,padx=10, pady=20)
txtunidades=Entry(frame1, width=20, font=('Arial',12))
txtunidades.grid(row=2,column=1)

lblcosto= Label(frame1, text='Correo', width=10)
lblcosto.grid(row=3,column=0,padx=10, pady=20)
txtcosto=Entry(frame1, width=20, font=('Arial',12))
txtcosto.grid(row=3,column=1)

lblempresa= Label(frame1, text='Telefono', width=10)
lblempresa.grid(row=4,column=0,padx=10, pady=20)
txtempresa=Entry(frame1, width=20, font=('Arial',12))
txtempresa.grid(row=4,column=1)

btnAgregar=Button(frame1,width=20,font=('Arial',12,'bold'),text='Agregar', 
                  bg='orange',bd=5,command=agregar_datos)
btnAgregar.grid(row=5,columnspan=2,padx=10,pady=20)

#Elementos del Frame2
lblArchivo=Label(frame2,text='Contenido',width=25,bg='gray16',
                 font=('Arial',12,'bold'),fg='white')
lblArchivo.grid(row=0,column=0,padx=10,pady=10)

tabla = ttk.Treeview(frame2,columns=( 'Apellidos','Edad','Correo','Telefono'))
tabla.grid(row=1,column=0)

tabla.column('#0',width=80)
tabla.column('Apellidos',width=80,anchor='center')
tabla.column('Edad',width=80,anchor='center')
tabla.column('Correo',width=80,anchor='center')
tabla.column('Telefono',width=80,anchor='center')

tabla.heading('#0', text='Nombres', anchor='center')
tabla.heading('Apellidos', text='Apellidos', anchor='center')
tabla.heading('Edad', text='Edad', anchor='center')
tabla.heading('Correo', text='Correo', anchor='center')
tabla.heading('Telefono', text='Telefono', anchor='center')

btnGuardar=Button(frame2,width=20,font=('Arial',12,'bold'),text='Mostrar',bg='green2',bd=5,command=mostrar_datos)
btnGuardar.grid(row=2,column=0,padx=10,pady=10)


ventana.mainloop()