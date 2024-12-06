#integral(a, b, x) Integral \(\int_{a}^{b} x \,dx\)

#type of questions

#ax^n + bx + c
#(ax + b)^n

#(qx)(bx + c)^n
#(px^m)(bx + c)^n
#(qx)(ax^m + c)^n

#(qx + r)(ax^m + bx + c)^n
#(qx)(sqrt(ax^2 + c))

#VARIABLES
# axn   pxm     a*x**n      p*x**m
# bx    px      b*x**2      p*x**2
# c     r       cx          rx

#INTEGRAL FORM
# (a/(n+1))*x**(n+1)
# (b/2)*x**2
# c*x

def axn (a: int, n: int) -> dict:
    n += 1
    if (a % n == 0):
        a //= n
    else:
        a /= n
    return {
        "a": a,
        # "x": "x",
        "n": n,
        # "res": f"{a}x^{n}"
    }

def bx (b: int) -> str:
    if (b % 2 == 0):
        b //= 2
    else:
        b /= 2
    return {
        "b": b,
        "n": 2,
        # "x": "x",
        # "res": f"{b}x"
    }

def c (c: int) -> str:
    return {
        "c": c,
        # "x": "x",
        # "res": f"{c}x"
    }

# def join (arr: list) -> str:
#     res = ""
#     for i, val in enumerate(arr):
#         if (i == 0):
#             res += f"{val} "
#         else:
#             if (val[0] == "-"):
#                 val = val[1:]
#                 res += "- "
#             else:
#                 res += "+ "
#             res += f"{val} "
#     return res

def main () -> None:
    #6x**2 - 2x + 7
    print(axn(6, 2))
    print(bx(-2))
    print(c(7))

main()