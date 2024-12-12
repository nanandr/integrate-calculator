from sympy import Symbol, sympify, integrate
from integral_sympy import calculate_integral  # Import dari integral_sympy
from integral_fix import integrate_expression  # Import dari integral_fix

# Fungsi untuk menghitung integral tak tentu atau tentu
def calculate_integral_gui(fx, lower=None, upper=None):
    x = Symbol('x')
    
    # Menghitung integral tak tentu dan tentu jika batas diberikan
    if lower is not None and upper is not None:
        # Untuk integral tentu
        result = integrate(fx, (x, lower, upper))
        return result
    else:
        # Untuk integral tak tentu
        full_integral, terms = calculate_integral(fx, x)  # Menggunakan integral_sympy
        return full_integral, terms
