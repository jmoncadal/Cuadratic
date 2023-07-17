class Quadratic:

    def __init__(self, equation):
        self.function = equation

    def roots(equation):

        sp_equation = equation.split(' ')
        global a, b, c

        if len(sp_equation[0]) == 3 and len(sp_equation[1]) > 2:
            a = 1
            b = int(sp_equation[1][:-1])
            c = int(sp_equation[2][:])
        
        if (len(sp_equation[1]) == 2 and '-' in sp_equation[1]):
            a = int(sp_equation[0][:-3])
            b = -1
            c = int(sp_equation[2][:])
        
        if (len(sp_equation[1]) == 2 and '+' in sp_equation[1]):
            a = int(sp_equation[0][:-3])
            b = 1
            c = int(sp_equation[2][:])

        else:
            a = int(sp_equation[0][:-3])
            b = int(sp_equation[1][:-1])
            c = int(sp_equation[2][:])

        global discriminant
        global sol, sol1, sol2

        discriminant = (b**2) - 4*a*c

        if discriminant < 0:
            sol1 = (-b + ((b**2) - 4*a*c)**(1/2)) / (2*a)
            sol2 = round(sol1, 2)
            sol2 = (-b - ((b**2) - 4*a*c)**(1/2)) / (2*a)
            sol2 = round(sol2)
            return '\nLa ecuación tiene soluciones, pero no reales. \nLas soluciones son: {sol1} y {sol2}\n'.format(sol1 = sol1, sol2 = sol2)

        elif discriminant == 0:
            sol = (-b + ((b**2) - 4*a*c)**(1/2)) / (2*a)
            sol = round(sol, 2)
            return '\nLa ecuación tiene una sola solución real.\nLa solución es: {solucion}\n'.format(solucion = sol)
            
        else:
            sol1 = (-b + ((b**2) - 4*a*c)**(1/2)) / (2*a)
            sol1 = round(sol1, 2)
            sol2 = (-b - ((b**2) - 4*a*c)**(1/2)) / (2*a)
            sol2 = round(sol2, 2 )
            return '\nLa ecuación tiene dos soluciones reales.\nLas soluciones son: {sol1} y {sol2}\n'.format(sol1 = sol1, sol2 = sol2)


    def vertex(equation):
        coord1 = -b / (2*a)
        coord2 = a*coord1**2 + b*coord1 + c
        coord1 = round(coord1, 2)
        coord2 = round(coord2, 2)
        return '\nEl vértice de la ecuación es: ({x}, {y})\n'.format(x = coord1, y = coord2)

    def saxis(equation):

        if discriminant < 0:
            s_axis = (sol1+sol2)/2
            s_axis = round(s_axis, 2)
            return'\nEl eje de simetría de la ecuación es: x = {s_axis}\n'.format(s_axis = s_axis)   
        
        elif discriminant == 0:
            s_axis = sol
            s_axis = round(s_axis, 2)
            return'\nEl eje de simetría de la ecuación es: x = {s_axis}\n'.format(s_axis = s_axis)
        
        else:
            s_axis = (sol1+sol2)/2
            s_axis = round(s_axis, 2)
            return'\nEl eje de simetría de la ecuación es: x = {s_axis}\n'.format(s_axis = s_axis)

eq = '3x^2 -3x -10'
print(Quadratic.roots(eq))
print(Quadratic.vertex(eq))
print(Quadratic.saxis(eq))
