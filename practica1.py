import tkinter as Tk
from tkinter import ttk
from tkinter import Menu
from tkinter import scrolledtext
from tkinter import messagebox as mBox 

ventana=Tk.Tk()
ventana.title("Sistema Escolar")

#barra de menu
def funcion_salir():
    ventana.quit()
    ventana.destroy()
    exit()
def funcion_acerca():
    mBox.showinfo('Acerca de','Nombre: Alondra Zarco Mercado\n\nCarrera: Ing.Sistemas Computacionales\n\nMateria: Topicos Avanzados de Programación')
def funcion_imprimir():
    if obj.get()=="" or opcion.get()==0  or opc_1.get()==0 and opc_2.get()==0 and opc_3.get()==0 or nombre.get()=="" or apellidop.get()=="" or apellidom.get()=="" or direccion.get()=="":
        mBox.showinfo('Datos Generales','Datos incompletos')    
    else:
        if opcion.get()==1: cad1="Soltero"
        if opcion.get()==2: cad1="Casado"
        if opcion.get()==3: cad1="Viudo"
        cade="\n\nPasatiempos:\n"
        if opc_1.get()!=0: cade+="Leer   "
        if opc_2.get()!=0: cade+="Ver Peliculas   "
        if opc_3.get()!=0: cade+="Redes Sociales"
        cade+="\n\nEstado Civil:\n"
        cade+=cad1+"\n\nObjetivo de la vida:\n"+obj.get()
        cad="Nombre: "+nombre.get()+"\n\nApellido P: "+apellidop.get()+"\n\nApellido M: "+apellidom.get()+"\n\nDirección: "+direccion.get()+"\n\nColonia: "+colonia.get()+"\n\nCiudad: "+ciudad.get()+"\n\nMunicipio: "+municipio.get()
        cad+=cade
        mBox.showinfo('Datos',cad) 

barra_menu=Menu(ventana)
ventana.config(menu=barra_menu)

opc_menu=Menu(barra_menu,tearoff=0)
opc_menu.add_separator()
opc_menu.add_command(label="Imprimir",command=funcion_imprimir)
opc_menu.add_separator()
opc_menu.add_command(label="Salir",command=funcion_salir)
barra_menu.add_cascade(label="Sistemas",menu=opc_menu)

opc_menu2=Menu(barra_menu,tearoff=0)
opc_menu2.add_separator()
opc_menu2.add_command(label="Acerca de",command=funcion_acerca)
barra_menu.add_cascade(label="Ayuda",menu=opc_menu2)


#pestaña 1
tabControl=ttk.Notebook(ventana)
tab1=ttk.Frame(tabControl)
tabControl.add(tab1,text="Datos Personales")
tabControl.pack(expand=1,fill="both")

ttk.Label(tab1,text="Nombre:  \n").grid(column=0,row=0)
ttk.Label(tab1,text="Apellido P. \n ").grid(column=0,row=1)
ttk.Label(tab1,text="Apellido M.  \n").grid(column=0,row=2)
ttk.Label(tab1,text="Dirección  \n").grid(column=0,row=3)
ttk.Label(tab1,text="Colonia  \n").grid(column=0,row=4)
ttk.Label(tab1,text="Ciudad \n ").grid(column=0,row=5)
ttk.Label(tab1,text="Municipio  \n").grid(column=0,row=6)

#entrada de datos
nombre=Tk.StringVar()
p_nombre=ttk.Entry(tab1,width=15,textvariable=nombre).grid(column=1,row=0)
apellidop=Tk.StringVar()
p_apellidop=ttk.Entry(tab1,width=15,textvariable=apellidop).grid(column=1,row=1)
apellidom=Tk.StringVar()
p_apellidom=ttk.Entry(tab1,width=15,textvariable=apellidom).grid(column=1,row=2)
direccion=Tk.StringVar()
p_direccion=ttk.Entry(tab1,width=20,textvariable=direccion).grid(column=1,row=3)

#lista despegable
colonia=Tk.StringVar()
s_colonia=ttk.Combobox(tab1,width=20,textvariable=colonia)
s_colonia["values"]=("Lomas de Morelia","Independencia","Manantiales","Satelite")
s_colonia.grid(column=1,row=4)
s_colonia.current(0)

ciudad=Tk.StringVar()
s_ciudad=ttk.Combobox(tab1,width=20,textvariable=ciudad)
s_ciudad["values"]=("Morelia","Patzcuaro","Quiroga","Zitacuaro")
s_ciudad.grid(column=1,row=5)
s_ciudad.current(0)

municipio=Tk.StringVar()
s_municipio=ttk.Combobox(tab1,width=20,textvariable=municipio)
s_municipio["values"]=("Tarimbaro","Acuitzeo","Ario de Rosales","Cuitzeo")
s_municipio.grid(column=1,row=6)
s_municipio.current(0)

#funcion boton
def funcion_click():
    if nombre.get()=="" or apellidop.get()=="" or apellidom.get()=="" or direccion.get()=="":
        accion.configure(text="Imprimir Datos Personales")
        ttk.Label(tab1,text="No se han llenado todos los datos").grid(column=1,row=8)
    else:
        cad="Nombre: "+nombre.get()+"\n\nApellido P: "+apellidop.get()+"\n\nApellido M: "+apellidom.get()+"\n\nDirección: "+direccion.get()+"\n\nColonia: "+colonia.get()+"\n\nCiudad: "+ciudad.get()+"\n\nMunicipio: "+municipio.get()
        accion.configure(text="Registro completo")
        mBox.showinfo('Datos',cad)
        ttk.Label(tab1,text=".                                                          .").grid(column=1,row=8)


#boton para registar
accion=ttk.Button(tab1,text="Imprimir Datos Personales",command=funcion_click)
accion.grid(column=1,row=7)

#pestaña2
tab2=ttk.Frame(tabControl)
tabControl.add(tab2,text="Datos Extras")

#checkbutton de pasatiempos
ttk.Label(tab2,text="Pasatiempos").grid(column=0,row=0)
opc_1=Tk.IntVar()
c_1=Tk.Checkbutton(tab2,text="Leer",variable=opc_1)
c_1.grid(column=0,row=1,sticky=Tk.W)
opc_2=Tk.IntVar()
c_2=Tk.Checkbutton(tab2,text="Ver Peliculas",variable=opc_2)
c_2.grid(column=1,row=1,sticky=Tk.W)
opc_3=Tk.IntVar()
c_3=Tk.Checkbutton(tab2,text="Redes Sociales",variable=opc_3)
c_3.grid(column=2,row=1,sticky=Tk.W)

#Radiobutton de estado civil 
ttk.Label(tab2,text="Estado Civil").grid(column=0,row=2)
opcion=Tk.IntVar()
rad1=Tk.Radiobutton(tab2,text="Soltero",variable=opcion,value=1)
rad1.grid(column=0,row=3,sticky=Tk.W)
rad2=Tk.Radiobutton(tab2,text="Casado",variable=opcion,value=2)
rad2.grid(column=1,row=3,sticky=Tk.W)
rad3=Tk.Radiobutton(tab2,text="Viudo",variable=opcion,value=3)
rad3.grid(column=2,row=3,sticky=Tk.W)
#objetivo de la vida
ttk.Label(tab2,text="\nObjetivo de la vida:   ").grid(column=0,row=4)
obj=Tk.StringVar()
p_obj=ttk.Entry(tab2,width=20,textvariable=obj).grid(column=0,row=5)

#boton imprimir datos
def funcion_click2():
    cad1=""
    if  obj.get()=="" or opcion.get()==0  or opc_1.get()==0 and opc_2.get()==0 and opc_3.get()==0:
        ac2.configure(text="imprimir Datos Extras")
        ttk.Label(tab2,text="No se han llenado todos los datos").grid(column=2,row=5)
    else:
        if opcion.get()==1: cad1="Soltero"
        if opcion.get()==2: cad1="Casado"
        if opcion.get()==3: cad1="Viudo"
        cade="\n\nPasatiempos:\n"
        if opc_1.get()!=0: cade+="Leer   "
        if opc_2.get()!=0: cade+="Ver Peliculas   "
        if opc_3.get()!=0: cade+="Redes Sociales"
        cade+="\n\nEstado Civil:\n"
        cade+=cad1+"\n\nObjetivo de la vida:\n"+obj.get()
        ac2.configure(text="Registro completo")
        mBox.showinfo('Datos Extras',cade)
        ttk.Label(tab2,text=".                                                        .").grid(column=2,row=5)
       
ac2=ttk.Button(tab2,text="Imprimir Datos Extras",command=funcion_click2)
ac2.grid(column=2,row=6)

ventana.mainloop()






