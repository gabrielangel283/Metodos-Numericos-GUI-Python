from tkinter import *
from tkinter import messagebox # usado para generar ventanas emergentes
from tkinter import ttk # usar el combobox
from metd_Biseccion import *
from metd_FalsaPosicion import *
from metd_NewtonRaphson import *

# Creando una ventana
ventana = Tk()

# Insertando el titulo de la ventana
ventana.title("IGU - Metodo de la biseccion")

# Asignar las dimensiones de la interfaz
ventana.geometry("560x560")

# Retringir la modificacion de las dimensiones
ventana.resizable(0, 0) # (ancho, alto) de la interfaz, 0 para no modificarlo

# Paneles para los elementos
panelCabecera = Frame(ventana, width=540, height=90, relief="ridge", borderwidth=2)
panelCabecera.place(x=10, y= 10)
panelPrincipal = Frame(ventana, width=540, height=440, relief="groove", borderwidth=2)
panelPrincipal.place(x=10, y= 110)

# comenzar el proceso
def comenzar():
    try:
        if cboMetodo.get() == "Bisección":
            for wid in panelPrincipal.winfo_children():
                wid.destroy()
            obj = metd_Biseccion(panelPrincipal)
            obj.mostrarCampos()

        if cboMetodo.get() == "Falsa Posición":
            for wid in panelPrincipal.winfo_children():
                wid.destroy()
            obj = metd_FalsaPosicion(panelPrincipal)
            obj.mostrarCampos()
        
        if cboMetodo.get() == "Newton-Raphson":
            for wid in panelPrincipal.winfo_children():
                wid.destroy()
            obj = metd_NewtonRaphson(panelPrincipal)
            obj.mostrarCampos()
        
    except Exception as e:
        messagebox.showinfo("Error", e)
        


# ETIQUETAS
lblTitulo = Label(panelCabecera, text="MÉTODOS NUMÉRICOS", font=("Arial", 18, "bold italic"))
lblTitulo.place(x=284, y=25, anchor="center")

lblMetodo = Label(panelCabecera, text="Seleccione el método: ", font=("Times New Roman", 10, "bold"))
lblMetodo.place(x=10, y=55)

# COMBO
cboMetodo = ttk.Combobox(panelCabecera, state="readonly")
cboMetodo.place(x=150, y=55)
cboMetodo["values"] = ("Bisección", "Falsa Posición", "Newton-Raphson")
cboMetodo.current(0)

# BOTONES
cboComenzar = Button(panelCabecera, text="COMENZAR", command=comenzar)
cboComenzar.place(x=320, y =53)

ventana.mainloop()