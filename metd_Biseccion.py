from tkinter import *
from tkinter import messagebox # usado para generar ventanas emergentes
from clases_Metod_Numericos.Clase_Biseccion import *

class metd_Biseccion():
    def __init__(self, panel):
        self.panel = panel
    
    def mostrarCampos(self):
        # ETIQUETAS
        lblTitulo = Label(self.panel, text="MÉTODO DE BISECCIÓN", fg="red", font=("Arial", 12, "bold italic"))
        lblTitulo.place(x=280, y=20 ,anchor="center")

        lblFuncion = Label(self.panel, text="Ingrese una funcion: ", font=("Times New Roman", 10, "bold"))
        lblFuncion.place(x=10, y=45)

        lblInferior = Label(self.panel, text="Intervalo inferior: ", font=("Times New Roman", 10, "bold"))
        lblInferior.place(x=10, y=80)
        lblSuperior = Label(self.panel, text="Intervalo superior: ", font=("Times New Roman", 10, "bold"))
        lblSuperior.place(x=10, y=115)

        lblToleracia = Label(self.panel, text="Tolerancia: ", font=("Times New Roman", 10, "bold"))
        lblToleracia.place(x=10, y=150)

        lblResultado = Label(self.panel, bg="sky blue")
        lblResultado.place(x=10, y = 185, width=518, height=245)


        # CAJAS DE TEXTO
        txtFuncion = Entry(self.panel)
        txtFuncion.place(x=140, y=45, width=180)

        txtInferior = Entry(self.panel)
        txtInferior.place(x=140, y=80, width=80)

        txtSuperior = Entry(self.panel)
        txtSuperior.place(x=140, y=115, width=80)

        txtTolerancia = Entry(self.panel)
        txtTolerancia.place(x=140, y=150, width=80)

        # METODOS AUXILIARES
        def tieneEspacios_O_estaVacio(cadena:str):
            return " " in cadena or len(cadena.strip()) == 0

        # PROCESO
        def procesar():
            if (tieneEspacios_O_estaVacio(txtFuncion.get()) or tieneEspacios_O_estaVacio(txtInferior.get()) or
            tieneEspacios_O_estaVacio(txtSuperior.get()) or tieneEspacios_O_estaVacio(txtTolerancia.get())):
                messagebox.showinfo("Informacion", "Recomendaciones: \n" + 
                "♠ No debe haber espacios de ningun tipo en cualquiera de los campos\n" +
                "♠ Todos los campos deben ser ingresados\n")
            else:
                try:
                    f = txtFuncion.get()
                    a = float(txtInferior.get())
                    b = float(txtSuperior.get())
                    tol = float(txtTolerancia.get())
                    obj = Biseccion(a, b, f, tol)
                    resultado = obj.proceso()
                    lblResultado.config(text=resultado, anchor="center", justify="center")
                except Exception as ex:
                    messagebox.showinfo("!ERROR¡", f"Error especifico: {ex}\n" + "\n"
                    "Recomendaciones: \n" + 
                    "♦ La función debe ser escrita usando la variable simbólica del programa -> 'x'\n" +
                    "♦ La función debe ser escrita con la sintaxis de python\n" + 
                    "♦ El valor del inter.inf < inter.sup\n" + 
                    "♦ La tolerancia debe ser mayor a 0 y menor a 1")


        # BOTONES
        btnProcesar = Button(self.panel, text="Procesar", font=("Times New Roman", 12, "bold"), command=procesar)
        btnProcesar.place(x=250, y=100)

        

        
            






