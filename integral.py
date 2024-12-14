from sympy import Symbol, integrate, sympify, expand

def integrate_steps (expression, x): # 6*x**2 - 2*x + 7
    expanded = expand(expression)
    terms = [] # [{"original":[6, 2], "integral":[2, 3]}, ..]
    original_terms = expanded.as_ordered_terms() # [6*x**2, -2*x, 7]
    
    for term in original_terms:
        coeff, exponent = term.as_coeff_exponent(x) # [6, 2] [-2, 1] [7, 0]

        integral_exponent = exponent + 1
        integral_coeff = coeff / integral_exponent
        terms.append({
            "original": [coeff, exponent],
            "integral": [integral_coeff, integral_exponent]
        })

    return {
        "expanded": expanded,
        "terms": terms
    }