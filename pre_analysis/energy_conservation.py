import sympy

def taylor(expr, vari, terms):
    return sum(
        [
        expr.diff(
            vari, i
            ).subs(
            vari, 0
            )*(
            vari**i/sympy.factorial(i)
            ) for i in xrange(0,terms)
        ]
        )

def euler_err():
    v = sympy.symbols('v', real=True)
    h, x = sympy.symbols('h x', real=True, positive=True)
    # u = x**2/2
    u = sympy.exp(-x)*x**(-1)
    a = -u.diff(x)
    te1 = u+v**2/2
    x2 = x+v*h
    v2 = v+a*h
    te2 = u.subs(x, x2) + v2**2/2
    print('energy expressions')
    sympy.pprint(te1)
    sympy.pprint(te2)
    print('difference')
    discrep = (te2-te1)
    sympy.pprint(discrep)
    # h_terms = discrep.expand(h).collect(h)
    # gauss_terms = discrep.expand(h).collect(u)
    # sympy.pprint(h_terms)
    # sympy.pprint(gauss_terms)
    # sympy.pprint(h_terms.coeff(h, 0))
    # sympy.pprint(gauss_terms.coeff(u, 1))
    # dominant = gauss_terms.coeff(u, 1)
    approx = taylor(discrep, h, 4)
    print('taylor to 4th order')
    sympy.pprint(approx)
    sympy.pprint(approx.collect(h))
    print('or')
    sympy.pprint(approx.simplify().expand().collect(h))
    try:
        maxA
    except NameError:
        maxA=None
    if maxA != None:
        print('discrep at max acceleration')
        sympy.pprint(maxA)
        sympy.pprint(approx.expand(h).subs(x, maxA))
    # sympy.pprint(discrep.diff(x))
    # sympy.pprint(discrep.diff(x).subs(x, maxA))
    # sympy.pprint(discrep.diff(x).subs(x, 0))
    # sympy.pprint(
    #     (
    #         discrep.diff(x).subs(x, maxA)
    #         -discrep.diff(x).subs(x, 0)
    #     ).simplify().collect(v).subs(h, .1)
    #     )

    # sympy.pprint(sympy.solve(discrep.diff(x),x))

    return
def verlet_err():
    v = sympy.symbols('v', real=True)
    h, x = sympy.symbols('h x', real=True, positive=True)
    # u = x**2/2
    u = sympy.exp(-x)*x**(-1)
    a = -u.diff(x)
    te1 = u+v**2/2
    x2 = x + v*h + a*h**2/2
    v2 = v+(a+a.subs(x, x2))*h/2
    te2 = u.subs(x, x2) + v2**2/2
    print('energy expressions')
    sympy.pprint(te1)
    sympy.pprint(te2)
    print('approximate difference at small h')
    discrep = (te2-te1)
    # sympy.pprint(discrep)
    # sympy.pprint(discrep.expand(h).collect(h))
    # gauss_terms = discrep.expand().collect(u)
    # sympy.pprint(gauss_terms)
    approx = taylor(discrep, h, 4)
    sympy.pprint(approx.expand().collect(h))
    # cubic_coeff=approx.coeff(h, 3).expand().collect(u)
    # sympy.pprint(cubic_coeff)
    try:
        maxA
    except NameError:
        maxA=None
    if maxA != None:
        print('discrepancy at max acceleration')
        sympy.pprint(maxA)
        sympy.pprint(approx.subs(x, maxA))

    return

if __name__ == '__main__':
    euler_err()
    # verlet_err()
