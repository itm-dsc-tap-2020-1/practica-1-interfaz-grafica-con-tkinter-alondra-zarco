import tkinter as Tk
from tkinter import ttk
from tkinter import Menu
from tkinter import scrolledtext
from tkinter import messagebox as mBox 

ventana=Tk.Tk()
ventana.title("EXAMEN DE ETICA")

#textos
ttk.Label(ventana,text="1.¿Que es la etica?:  \n").grid(column=0,row=0)
ttk.Label(ventana,text="2.¿Quien es el denominado padre de la etica? \n ").grid(column=0,row=1)


#entry
pre1=Tk.StringVar()
p_1=ttk.Entry(ventana,width=15,textvariable=pre1).grid(column=1,row=0)
pre2=Tk.StringVar()
p_2=ttk.Entry(ventana,width=15,textvariable=pre2).grid(column=1,row=1)

#radiobutton1
ttk.Label(ventana,text="\n3.Definicion etimologica de etica:").grid(column=0,row=2)
opcion=Tk.IntVar()
rad1=Tk.Radiobutton(ventana,text="Buen vivir",variable=opcion,value=1)
rad1.grid(column=0,row=3,sticky=Tk.W)
rad2=Tk.Radiobutton(ventana,text="Bien actuar",variable=opcion,value=2)
rad2.grid(column=1,row=3,sticky=Tk.W)
rad3=Tk.Radiobutton(ventana,text="Hacer el bien",variable=opcion,value=3)
rad3.grid(column=2,row=3,sticky=Tk.W)

#radiobutton2
ttk.Label(ventana,text="\n4.Otra forma de referirse a la eutanasia es: ").grid(column=0,row=4)
opcion2=Tk.IntVar()
rad1=Tk.Radiobutton(ventana,text="Muerte piadosa",variable=opcion2,value=1)
rad1.grid(column=0,row=5,sticky=Tk.W)
rad2=Tk.Radiobutton(ventana,text="Buen morir",variable=opcion2,value=2)
rad2.grid(column=1,row=5,sticky=Tk.W)
rad3=Tk.Radiobutton(ventana,text="Muerte asistida",variable=opcion2,value=3)
rad3.grid(column=2,row=5,sticky=Tk.W)

#checkbutton
ttk.Label(ventana,text="\n5. Acciones eticamente correctas").grid(column=0,row=6)
opc_1=Tk.IntVar()
c_1=Tk.Checkbutton(ventana,text="Robar",variable=opc_1)
c_1.grid(column=0,row=7,sticky=Tk.W)
opc_2=Tk.IntVar()
c_2=Tk.Checkbutton(ventana,text="Burlarse",variable=opc_2)
c_2.grid(column=1,row=7,sticky=Tk.W)
opc_3=Tk.IntVar()
c_3=Tk.Checkbutton(ventana,text="Ayudar",variable=opc_3)
c_3.grid(column=2,row=7,sticky=Tk.W)
opc_4=Tk.IntVar()
c_4=Tk.Checkbutton(ventana,text="Donar",variable=opc_4)
c_4.grid(column=3,row=7,sticky=Tk.W)
opc_5=Tk.IntVar()
c_5=Tk.Checkbutton(ventana,text="Defraudar",variable=opc_5)
c_5.grid(column=4,row=7,sticky=Tk.W)

#funcion boton
def funcion_click():
    cal=0
    if pre1.get()=="Es la ciencia que estudia el comportamiento humano": cal+=20
    if pre2.get()=="Karl Marx": cal+=20
    if opcion.get()==2: cal+=20
    if opcion2.get()==3: cal+=20 
    if opc_3.get()!=0 or opc_4.get()!=0: cal+=20
    if opc_1.get()!=0 or opc_2.get()!=0 or opc_5.get()!=0 :cal-=20
    

    mBox.showinfo('Calificacion total',cal)
    


#boton para registar
accion=ttk.Button(ventana,text="Calificar",command=funcion_click)
accion.grid(column=1,row=8)


ventana.mainloop()