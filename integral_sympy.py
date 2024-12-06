from sympy import Symbol, integrate

def coeff_exponent (i, x):
    a = i.as_coeff_exponent(x)[0]
    n = i.as_coeff_exponent(x)[1]

    print(f"a*x**n = {i}")
    print(f"a = {a}")
    print(f"n = {n}")
    print()
    print(f"a = a / n + 1 = {a / (n + 1)}")
    print(f"n = n + 1 = {n + 1}")
    print()

def main ():
    #sympy.sympify("6x**2-2x+7")
    x = Symbol('x')
    
    axn = 6 * x ** 2
    coeff_exponent(axn, x)

    bx = - 2 * x
    coeff_exponent(bx, x)

    c = 7

    print(integrate(axn + bx + c, x))

main()