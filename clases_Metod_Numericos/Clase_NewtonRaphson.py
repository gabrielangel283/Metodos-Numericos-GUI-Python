from sympy import Symbol
from sympy import sympify
from sympy import lambdify
from sympy import diff


class Newton_Raphson():
    def __init__(self, puntoInicial, funcion, tol):
        if 0<tol and tol<1:
            self.puntoInicial = puntoInicial
            self.funcion = funcion
            self.tol = tol
        else:
            raise ValueError("La tolerancia ingresada es invalida")
    
    def proceso(self):
        x = Symbol("x")
        fn = sympify(self.funcion)
        d_fn = diff(fn, x)
        f = lambdify(x, fn) # funcion en donde se reemplazara el valor
        df = lambdify(x, d_fn) # derivada de la funcion donde se reemplazara el valor
        ea = 1
        x_anterior = self.puntoInicial
        x_nuevo = 0
        i = 0
        cadenaFinal = ""

        # METODO DE NEWTON-RAPSHON
        if df(x_anterior)!=0:
            cadenaFinal = ("{:^30}".format("METODO DE NEWTON-RAPHSON") + "\n" + 
                        "{:^25} {:^25} {:^25}".format("i", "pi", "er(%)") + "\n" +
                        "{:^25} {:^25f} {:^25}".format(i, x_anterior, "0.00000000")) + "\n"
            
            while self.tol < ea:
                x_nuevo = x_anterior - f(x_anterior)/df(x_anterior)

                ea = abs(x_nuevo-x_anterior)/x_nuevo
                i += 1

                cadenaFinal += "{:^25} {:^25f} {:^25f}".format(i, x_nuevo, round(ea*100, 9)) + "\n"

                x_anterior = x_nuevo

        else:
            cadenaFinal = "El punto inicial que ingreso no sirve para el metodo" + "\n"
        
        cadenaFinal += f"\nEl valor aproximado de x es: {round(x_anterior, 9)}, con error de {round(ea*100,9)}%"

        return cadenaFinal




