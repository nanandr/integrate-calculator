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

def integrate_subs (expression, x, n): # 3*x**3 - 6*x**2 + 4*x, x, -1
    return expression.subs(x, n)

def format_terms (terms):
    res = []

    for term in terms:
        coeff = term["original"][0]
        exponent = term["original"][1]

        integral_coeff = term["integral"][0]
        integral_exponent = term["integral"][1]

        res.append(f"{coeff}*x**{exponent} -> {integral_coeff}*x**{integral_exponent}")
        res.append(f"a -> a/(n+1) = {coeff}/({exponent}+1) = {integral_coeff}")
        res.append(f"n -> n+1 = {exponent}+1 = {integral_exponent}\n")

    return res

def format_subs (terms, limit):
    res = []

    for term in terms:
        coeff = term["integral"][0]
        exponent = term["integral"][1]

        res.append(f"{coeff}*{limit}**{exponent} = {coeff*limit**exponent}")

    return res