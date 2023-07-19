import numpy as np
import matplotlib.pyplot as plt

class Quadratic:

    def __init__(self, equation):
        self.function = equation

    def roots(equation):
        global a, b, c
        global discriminant
        global sol, sol1, sol2

        sp_equation = equation.split(' ')

        if len(sp_equation[0]) == 3 and len(sp_equation[1]) > 2:
            a = 1
            b = int(sp_equation[1][:-1])
            c = int(sp_equation[2][:])
        
        elif (len(sp_equation[1]) == 2 and '-' in sp_equation[1]):
            a = int(sp_equation[0][:-3])
            b = -1
            c = int(sp_equation[2][:])
        
        elif (len(sp_equation[1]) == 2 and '+' in sp_equation[1]):
            a = int(sp_equation[0][:-3])
            b = 1
            c = int(sp_equation[2][:])

        else:
            a = int(sp_equation[0][:-3])
            b = int(sp_equation[1][:-1])
            c = int(sp_equation[2][:])

        discriminant = (b**2) - 4*a*c

        if discriminant < 0:
            sol1 = (-b + ((b**2) - 4*a*c)**(1/2)) / (2*a)
            sol2 = sol1
            sol2 = (-b - ((b**2) - 4*a*c)**(1/2)) / (2*a)
            sol2 = sol2
            return '\nLa ecuación tiene soluciones, pero no reales. \nLas soluciones son: {sol1} y {sol2}\n'.format(sol1 = sol1, sol2 = sol2)

        elif discriminant == 0:
            sol = (-b + ((b**2) - 4*a*c)**(1/2)) / (2*a)
            sol = round(sol, 3)
            return '\nLa ecuación tiene una sola solución real.\nLa solución es: {solucion}\n'.format(solucion = sol)
            
        else:
            sol1 = (-b + ((b**2) - 4*a*c)**(1/2)) / (2*a)
            sol1 = round(sol1, 3)
            sol2 = (-b - ((b**2) - 4*a*c)**(1/2)) / (2*a)
            sol2 = round(sol2, 3)
            return '\nLa ecuación tiene dos soluciones reales.\nLas soluciones son: {sol1} y {sol2}\n'.format(sol1 = sol1, sol2 = sol2)
    
    def vertex(equation):
        global coord1, coord2

        coord1 = -b / (2*a)
        coord2 = a*coord1**2 + b*coord1 + c
        coord1 = round(coord1, 3)
        coord2 = round(coord2, 3)
        return '\nEl vértice de la ecuación es: ({x}, {y})\n'.format(x = coord1, y = coord2)

    def saxis(equation):

        global s_axis

        if discriminant < 0:
            s_axis = (sol1+sol2)/2
            s_axis = s_axis
            return'\nEl eje de simetría de la ecuación es: x = {s_axis}\n'.format(s_axis = s_axis)   
        
        elif discriminant == 0:
            s_axis = sol
            s_axis = round(s_axis, 3)
            return'\nEl eje de simetría de la ecuación es: x = {s_axis}\n'.format(s_axis = s_axis)
        
        else:
            s_axis = (sol1+sol2)/2
            s_axis = round(s_axis, 3)
            return'\nEl eje de simetría de la ecuación es: x = {s_axis}\n'.format(s_axis = s_axis)
        
    def plot(equation, nvalue = -12, pvalue = 12):
        fig, ax = plt.subplots(figsize = (10, 5), dpi = 136)
        x = np.linspace(nvalue, pvalue, 100)
        y = a*x**2+b*x+c

        ax.grid(True)
        ax.set_xlabel('$x$')
        ax.set_ylabel('$y$')
        ax.set_title('Graph of ${eq}$'.format(eq = equation))

        plt.axhline(y = 0, color = 'r', linestyle = '--')
        plt.axvline(x = 0, color = 'r', linestyle = '--')
        ax.plot(x, y)

        if discriminant < 0:
            plt.plot(coord1, coord2, marker = 'o', markersize = 5, color = 'black', label = 'Vertex: ({coord1}, {coord2})'.format(coord1 = coord1, coord2 = coord2))
        
        elif discriminant == 0:
            plt.plot(sol, 0, marker = 'o', markersize = 5, color = 'black', label ='Solution: {sol1}'.format(sol1 = sol1))
            plt.plot(coord1, coord2, marker = 'o', markersize = 5, color = 'black', label = 'Vertex: ({coord1}, {coord2})'.format(coord1 = coord1, coord2 = coord2))

        else:
            plt.plot(sol1, 0, marker = 'o', markersize = 5, color = 'black', label ='Solution 1: {sol1}'.format(sol1 = sol1))
            plt.plot(sol2, 0, marker = 'o', markersize = 5, color = 'black', label ='Solution 2: {sol2}'.format(sol2 = sol2))
            plt.plot(coord1, coord2, marker = 'o', markersize = 5, color = 'black', label = 'Vertex: ({coord1}, {coord2})'.format(coord1 = coord1, coord2 = coord2))

        plt.legend()
        plt.show()

eq = '3x^2 -5x -100'
eq1 = 'x^2 -5x -100'
print(Quadratic.roots(eq))
print(Quadratic.vertex(eq))
print(Quadratic.saxis(eq))
print(Quadratic.plot(eq))
print(Quadratic.plot(eq1))

