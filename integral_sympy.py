from sympy import Symbol, integrate, sympify, expand

def split (expression, x):
    expression = expand(expression)
    print(f"f(x) = {expression}") # print expanded terms
    print()
    return expression.as_ordered_terms()

def coeff_exponent (exp, x): # get coefficient and exponent from terms
    terms = split(exp, x)
    print(terms) # print terms as list
    for term in terms:
        print("Term:")
        print(f"a*x**n = {term}")
        a, n = term.as_coeff_exponent(x) # get coefficient & exponent from term
        
        print(f"a = {a}")
        print(f"n = {n}")
        print()

        print("Integrate:")
        print(f"a / (n + 1) = {a} / ({n} + 1) = {a / (n + 1)}") # integrate coefficient
        print(f"n + 1 = {n} + 1 = {n + 1}") # integrate exponent
        print(f"{term} = {a / (n + 1)}*x**{n+1}") # print integrated term 
        print()
        print()

def main ():
    x = Symbol('x')
    
    while True:
        calculate = input("f(x) = ")
        coeff_exponent(sympify(calculate), x)
        print(integrate(sympify(calculate), x))
        print()

main()