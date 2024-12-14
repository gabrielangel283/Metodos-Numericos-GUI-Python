from sympy import Symbol
from sympy import sympify
from sympy import lambdify

class Biseccion():
    def __init__(self, inf, sup, funcion, tol):
        if inf<sup and tol>0 and tol<1:
            self.inf = inf
            self.sup = sup
            self.funcion = funcion
            self.tol = tol
        else:
            raise ValueError("El valor de inferior, superior o tolerancia es invalido")
        

    def proceso(self):
        x = Symbol("x") # x - variable simbolica
        fn = sympify(self.funcion) # fn - la funcion ingresada
        f = lambdify(x,fn) # f(a) - la funcion ingresada evaluada en el punto a
        a = self.inf # intervalo inferior
        b = self.sup # intervalo superior
        ea = 1 # error absoluto
        x_anteriror = 0
        i = 1 # contador de iteraciones
        xr = 0
        cadenaFinal = ""

        # cabecera
        
        if f(a)*f(b)<0:
            cadenaFinal = ("{:^20}".format("Metodo de Biseccion") + "\n" + 
                        "{:^30} {:^29} {:^30} {:^30} {:^31}".format("i", "a", "b", "xr", "er(%)") + "\n" + 
                        "{:^25} {:^25f} {:^25f} {:^25f} {:^25}".format(i, a, b, (a+b)/2, "0.000000000")) + "\n"

            while self.tol < ea:
                xr = (a+b)/2

                if f(a)*f(xr)<0:
                    b = xr
                elif f(a)*f(xr)>0:
                    a = xr
                else:
                    break
                x_anteriror = xr

                # imprime datos
                i += 1
                xr = (a+b)/2
                ea = abs((xr-x_anteriror)/xr)
                cadenaFinal += "{:^25} {:^25f} {:^25f} {:^25f} {:^25}".format(i, a, b, xr, round(ea*100, 9)) + "\n"

            if f(xr)==0:
                cadenaFinal += f"\nEl valor aproximado de x es: {round(xr, 9)}, con un error de 0%"
            else:
                cadenaFinal += f"\nEl valor aproximado de x es: {round(xr, 9)}, con un error de {round(ea*100,9)}%"
        elif f(a)*f(b)>0:
            cadenaFinal = "No existe solucion en el intervalo ingresado"
        else:
            cadenaFinal = "Uno de los intervalos es una solucion de la funcion ingresada"

        return str(cadenaFinal)