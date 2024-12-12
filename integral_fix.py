# integral_fix.py

# Fungsi untuk menghitung integral dari ax^n
def axn(a: int, n: int) -> dict:
    n += 1
    if a % n == 0:
        a //= n
    else:
        a /= n
    return {
        "a": a,
        "n": n,
    }

# Fungsi untuk menghitung integral dari bx (b*x^2)
def bx(b: int) -> dict:
    if b % 2 == 0:
        b //= 2
    else:
        b /= 2
    return {
        "b": b,
        "n": 2,
    }

# Fungsi untuk menghitung integral dari konstanta c
def c(c: int) -> dict:
    return {
        "c": c,
    }

# Fungsi untuk memproses ekspresi yang lebih kompleks
def integrate_expression(fx, x):
    result = []
    
    # Proses ax^n
    if 'x**' in fx:
        coeff, exp = fx.split('x**')
        result.append(axn(int(coeff), int(exp)))

    # Proses bx
    elif 'x' in fx:
        coeff = fx.split('x')[0]
        result.append(bx(int(coeff)))
    
    # Proses konstanta
    else:
        result.append(c(int(fx)))

    return result
