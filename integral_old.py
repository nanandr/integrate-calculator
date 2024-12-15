from gui.TkForge.gui import gui
from sympy import Symbol, integrate, sympify, expand

def write_lines (lines):
    return "\n".join(lines)

def expand_expression (expression):
    expanded = expand(expression)
    return {
        "lines": [f"f(x) = {expression}"],
        "res": expanded
    }

def coeff_exponent (term, x):
    a, n = term.as_coeff_exponent(x)
    return [a, n]

def process_term (term, x):
    a, n = coeff_exponent(term, x)

    integral_exponent = n + 1
    integral_coeff = a / integral_exponent

    return {
        "lines": [
            f"Term: {term}",
            "Coefficient:"
            f"a = {a}",
            "Exponent:",
            f"n = {n}",
            "Integration:",
            f"a / (n + 1) = {a} / ({n} + 1) = {integral_coeff}",
            f"n + 1 = {n} + 1 = {integral_exponent}",
            f"Integrated Term: {integral_coeff}*x**{integral_exponent}\n"
        ] 
    }

def integrate_expression (expression, x):
    expanded = expand_expression(expression)
    terms = expanded.as_ordered_terms()

    for term in terms:
        process_term(term, x)
    
    full_integral = integrate(expression, x)
    
    return {
        "res": full_integral,
        "str": [
            "Integrated Expression:",
            f"F(x) = {full_integral}"
        ]
    }

def main () -> None:
    return

    x = Symbol('x')
    while True:
        print("===============================")
        print("Integral Calculator")
        print("Type f(x) to start. Type 'exit' to close the application\n")
        user_input = input("f(x) = ")
        print()

        if user_input.lower() == "exit":
            break

        limits = []
        print("Limit:")
        print("Leave Blank if it's indefinite integral\n")
        print("Lower Limit:")
        limits.append(input("l = "))
        print("Upper Limit:")
        limits.append(input("u = "))
        print()
        
        try:
            expression = sympify(user_input)
            f = integrate_expression(expression, x)
            if limits[0] != "" and limits[1] != "":
                lower_limit = sympify(limits[0])
                upper_limit = sympify(limits[1])

                # Calculate the definite integral directly
                definite_integral = integrate(expression, (x, lower_limit, upper_limit))

                # Substitute limits for manual verification
                fl = f.subs(x, lower_limit)
                fu = f.subs(x, upper_limit)

                # Display results
                print("Substitute Limits:")
                terms = f.as_ordered_terms()
                for limit, label in zip([lower_limit, upper_limit], ["Lower Limit", "Upper Limit"]):
                    print(f"\n{label} ({limit}):")
                    for term in terms:
                        a, n = coeff_exponent(term, x)
                        substituted = a * (limit ** n)
                        print(f"{term} -> {a}*{limit}**{n} = {substituted}")
                    result = f.subs(x, limit)
                    print(f"F({limit}) = {result}")

                # Display results
                print(f"\nF({upper_limit}) - F({lower_limit}) = {fu} - {fl} = {fu - fl}")
                print("\nDefinite Integral Result:")
                print(f"∫[{lower_limit}, {upper_limit}] f(x) dx = {definite_integral}\n")
        except Exception as e:
            print(f"Error: {e}\n Please enter a valid mathematical expression")

if __name__ == "__main__": 
    main()