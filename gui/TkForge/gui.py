# Code generated by TkForge <https://github.com/axorax/tkforge>
# Donate to support TkForge! <https://www.patreon.com/axorax>

import os
import sys
import tkinter as tk

from sympy import Symbol, integrate, sympify
from integral import integrate_steps

def writeLines (lines: list) -> str:
    return "\n".join(lines)

def gui ():
    def load_asset(path):
        base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        assets = os.path.join(base, "assets")
        return os.path.join(assets, path)

    def calculate ():
        x = Symbol('x')
        user_input_val = user_input.get("1.0", "end-1c")
        lower_limit_val = lower_limit.get()
        upper_limit_val = upper_limit.get()

        expression = sympify(user_input_val)

        res = integrate_steps(expression, x)
        canvas.itemconfig(steps, text=writeLines([
            "f(x) = ",
            "Expanded:"
            
        ]))

        if lower_limit_val.strip() != "" and upper_limit_val.strip() != "":
            f = str(integrate(expression, (x, sympify(lower_limit_val), sympify(upper_limit_val))))
        else:
            f = str(integrate(expression, x))
            f += " + c"
        canvas.itemconfig(answer, text=str(f))
        
        
    window = tk.Tk()
    window.geometry("600x800")
    window.configure(bg="#ffffff")
    window.title("Integral Calculator")

    canvas = tk.Canvas(
        window,
        bg = "#ffffff",
        width = 600,
        height = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x=0, y=0)

    image_1 = tk.PhotoImage(file=load_asset("1.png"))

    canvas.create_image(300, 423, image=image_1)

    image_2 = tk.PhotoImage(file=load_asset("2.png"))

    canvas.create_image(300, 23, image=image_2)

    upper_limit = tk.Entry(
        bd=0,
        fg="#000000",
        insertbackground="#FFFFFF",
        highlightthickness=0
    )

    upper_limit.place(x=56, y=73, width=26, height=19)

    image_3 = tk.PhotoImage(file=load_asset("3.png"))

    canvas.create_image(69, 130, image=image_3)

    lower_limit = tk.Entry(
        bd=0,
        fg="#000000",
        insertbackground="#FFFFFF",
        highlightthickness=0
    )

    lower_limit.place(x=56, y=168, width=26, height=19)

    image_4 = tk.PhotoImage(file=load_asset("4.png"))

    canvas.create_image(326, 130, image=image_4)

    user_input = tk.Text(
        bd=0,
        fg="#000000",
        insertbackground="#FFFFFF",
        highlightthickness=0
    )

    user_input.place(x=108, y=77, width=404, height=108)

    image_5 = tk.PhotoImage(file=load_asset("5.png"))

    canvas.create_image(304, 288, image=image_5)

    answer = canvas.create_text(
        139,
        279,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Inter", 16 * -1)
    )

    image_6 = tk.PhotoImage(file=load_asset("6.png"))

    canvas.create_image(304, 559, image=image_6)

    steps = canvas.create_text(
        70,
        380,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Inter", 16 * -1)
    )

    submit_image = tk.PhotoImage(file=load_asset("7.png"))

    submit = tk.Button(
        image=submit_image,
        relief="flat",
        borderwidth=0,
        highlightthickness=0,
        command=calculate
    )

    submit.place(x=373, y=209, width=180, height=43)

    window.resizable(False, False)
    window.mainloop()
