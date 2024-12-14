from tkinter import *
from tkinter import messagebox # usado para generar ventanas emergentes
from clases_Metod_Numericos.Clase_NewtonRaphson import *


class metd_NewtonRaphson():
    def __init__(self, panel):
        self.panel = panel
    
    def mostrarCampos(self):
        # ETIQUETAS
        lblTitulo = Label(self.panel, text="MÉTODO DE NEWTON-RAPHSON", fg="red", font=("Arial", 12, "bold italic"))
        lblTitulo.place(x=280, y=20 ,anchor="center")

        lblFuncion = Label(self.panel, text="Ingrese una funcion: ", font=("Times New Roman", 10, "bold"))
        lblFuncion.place(x=10, y=45)

        lblPosicionIncial = Label(self.panel, text="Punto de inicio", font=("Times New Roman", 10, "bold"))
        lblPosicionIncial.place(x=10, y=80)

        lblToleracia = Label(self.panel, text="Tolerancia: ", font=("Times New Roman", 10, "bold"))
        lblToleracia.place(x=10, y=115)

        lblResultado = Label(self.panel, bg="sky blue")
        lblResultado.place(x=10, y = 150, width=520, height=275)
    
        # CAJAS DE TEXTO
        txtFuncion = Entry(self.panel)
        txtFuncion.place(x=140, y=45, width=180)

        txtPuntoInicial = Entry(self.panel)
        txtPuntoInicial.place(x=140, y=80, width=180)

        txtTolerancia = Entry(self.panel)
        txtTolerancia.place(x=140, y=115, width=80)

        # METODOS AUXILIARES
        def tieneEspacios_O_estaVacio(cadena:str):
            return " " in cadena or len(cadena.strip()) == 0
    
        # PROCESO
        def procesar():
            if (tieneEspacios_O_estaVacio(txtFuncion.get()) or tieneEspacios_O_estaVacio(txtPuntoInicial.get()) 
                or tieneEspacios_O_estaVacio(txtTolerancia.get())):
                messagebox.showinfo("Informacion", "Recomendaciones: \n" + 
                "♠ No debe haber espacios de ningun tipo en cualquiera de los campos\n" +
                "♠ Todos los campos deben ser ingresados\n")
            else:
                try:
                    f = txtFuncion.get()
                    a = float(txtPuntoInicial.get())
                    tol = float(txtTolerancia.get())
                    obj = Newton_Raphson(a, f, tol)
                    resultado = obj.proceso()
                    lblResultado.config(text=resultado, anchor="center", justify="center")
                except Exception as ex:
                    messagebox.showinfo("!ERROR¡", f"Error especifico: {ex}\n" + "\n"
                    "Recomendaciones: \n" + 
                    "♦ La función debe ser escrita usando la variable simbólica del programa -> 'x'\n" +
                    "♦ La función debe ser escrita con la sintaxis de python\n" +  
                    "♦ La tolerancia debe ser mayor a 0 y menor a 1")



        # BOTONES
        btnProcesar = Button(self.panel, text="Procesar", font=("Times New Roman", 12, "bold"), command=procesar)
        btnProcesar.place(x=250, y=111)