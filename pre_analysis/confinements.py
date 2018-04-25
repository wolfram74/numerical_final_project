import sympy

def confinment1():
    h, b, x = sympy.symbols('h b x', real =True)
    potential = sympy.exp(-(x-b)) + sympy.exp(x-(h-b))
    sympy.pprint(potential)
    sympy.pprint(-potential.diff(x))


if __name__ =='__main__':
    confinment1()
