from sympy import Symbol, integrate, sympify, expand

def expand_expression (expression):
    expanded = expand(expression)
    print("Expanded Expression:")
    print(f"f(x) = {expression}\n") # print expanded terms
    return expanded

def split_to_terms (expression, x):
    terms = expression.as_ordered_terms()
    print(f"Terms: {terms}\n")
    return terms

def process_term (term, x):
    a, n = term.as_coeff_exponent(x)
    print(f"Term: {term}")
    print(f"Coefficient (a) = {a}")
    print(f"Exponent (n) = {n}")

    integral_exponent = n + 1
    integral_coeff = a / integral_exponent

    print("Integration:")
    print(f"a / (n + 1) = {a} / ({n} + 1) = {integral_coeff}")
    print(f"n + 1 = {n} + 1 = {integral_exponent}")
    print(f"Integrated Term: {integral_coeff} * x * {integral_exponent}\n")

def integrate_expression (expression, x):
    expanded = expand_expression(expression)
    terms = split_to_terms(expanded, x)
    for term in terms:
        process_term(term, x)
    
    full_integral = integrate(expression, x)
    print("Integrated Expression:")
    print(f"F(x) = {full_integral}\n")
    return full_integral

def main () -> None:
    x = Symbol('x')
    while True:
        print("===============================")
        print("Integral Calculator")
        print("Type f(x) to start. Type 'exit' to close the application\n")
        user_input = input("f(x) = ")
        print()

        if user_input.lower() == "exit":
            break
        
        try:
            expression = sympify(user_input)
            integrate_expression(expression, x)
        except Exception as e:
            print(f"Error: {e}\n Please enter a valid mathematical expression")

if __name__ == "__main__": 
    main()