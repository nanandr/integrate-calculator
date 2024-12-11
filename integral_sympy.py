from sympy import Symbol, integrate, sympify, expand

def coeff_exponent (exp, x): #get coefficient and exponent from all terms
    exp = expand(exp)
    print(f"f(x) = {exp}") # print expanded term
    print()
    terms = exp.as_ordered_terms()
    for term in terms:
        print("Term:")
        print(f"a*x**n = {term}")
        a, n = term.as_coeff_exponent(x) # coefficient & exponent
        
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