from sympy import Symbol, integrate, sympify, expand

# Fungsi untuk memecah ekspresi dan mencetaknya
def split(expression, x):
    expression = expand(expression)
    return expression.as_ordered_terms()

# Fungsi untuk mendapatkan koefisien dan eksponen dari setiap term
def coeff_exponent(exp, x):
    terms = split(exp, x)
    results = []
    
    for term in terms:
        a, n = term.as_coeff_exponent(x)
        results.append({
            "term": term,
            "coefficient": a,
            "exponent": n,
            "integral": a / (n + 1) if n != -1 else None  # Handle the case for x^-1
        })
    
    return results

# Fungsi untuk menghitung integral
def integrate_expression(expression, x):
    expr = sympify(expression)
    return integrate(expr, x)

# Fungsi utama untuk menghitung integral yang akan digunakan di GUI
def calculate_integral(fx, x):
    terms = coeff_exponent(fx, x)
    full_integral = integrate_expression(fx, x)
    
    return full_integral, terms
