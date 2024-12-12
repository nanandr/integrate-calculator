import tkinter as tk
from tkinter import messagebox
from main import calculate_integral_gui  # Mengimpor fungsi dari main.py

def main():
    # Inisialisasi jendela utama
    root = tk.Tk()
    root.title("Kalkulator Integral")
    root.geometry("600x450")  # Ukuran jendela
    root.configure(bg="#E6E6E6")  # Latar belakang abu-abu terang

    # Menambahkan judul aplikasi dengan font besar dan simbol integral
    title = tk.Label(root, text="Kalkulator Integral", bg="#E6E6E6", font=("Verdana", 22, "bold"), fg="#FF5733")
    title.grid(row=0, column=0, columnspan=3, pady=30, sticky="nsew")

    # Menambahkan simbol integral besar
    integral_symbol = tk.Label(root, text="∫", font=("Verdana", 60), fg="#FF5733", bg="#E6E6E6")
    integral_symbol.grid(row=1, column=0, columnspan=3, pady=10, sticky="nsew")

    # Label dan Entry untuk input fungsi
    tk.Label(root, text="Masukkan f(x):", bg="#E6E6E6", font=("Verdana", 14), fg="#333333").grid(row=2, column=1, pady=10, padx=10, sticky="w")
    fx_entry = tk.Entry(root, width=20, font=("Verdana", 14), bg="#ffffff", fg="#333333", relief="solid", bd=3)
    fx_entry.grid(row=2, column=2, pady=10, padx=10)

    # Label dan Entry untuk batas bawah dan atas
    tk.Label(root, text="Batas Bawah:", bg="#E6E6E6", font=("Verdana", 14), fg="#333333").grid(row=3, column=1, pady=10, padx=10, sticky="w")
    lower_entry = tk.Entry(root, width=20, font=("Verdana", 14), bg="#ffffff", fg="#333333", relief="solid", bd=3)
    lower_entry.grid(row=3, column=2, pady=10, padx=10)

    tk.Label(root, text="Batas Atas:", bg="#E6E6E6", font=("Verdana", 14), fg="#333333").grid(row=4, column=1, pady=10, padx=10, sticky="w")
    upper_entry = tk.Entry(root, width=20, font=("Verdana", 14), bg="#ffffff", fg="#333333", relief="solid", bd=3)
    upper_entry.grid(row=4, column=2, pady=10, padx=10)

    # Fungsi untuk menghitung integral
    def calculate_integral_gui_func():
        fx = fx_entry.get()
        lower = lower_entry.get()
        upper = upper_entry.get()

        # Mengubah input batas menjadi None jika tidak ada input batas
        lower = None if lower == "" else lower
        upper = None if upper == "" else upper

        try:
            # Menggunakan fungsi perhitungan dari file main.py
            result = calculate_integral_gui(fx, lower, upper)
            
            # Menampilkan hasil integral tak tentu
            result_message = f"Hasil Integral Tak Tentu:\n{result[0]}\n\nProses Integral:\n"
            for term in result[1]:
                result_message += f"\n{term}"
            
            # Jika ada batas, tampilkan hasil integral tentu
            if lower is not None and upper is not None:
                result_message += f"\n\nIntegral Tentu:\n{result}"

            messagebox.showinfo("Hasil Integral", result_message)
        except Exception as e:
            messagebox.showerror("Error", f"Kesalahan: {e}")

    # Tombol untuk menghitung integral
    calculate_button = tk.Button(root, text="Hitung Integral", command=calculate_integral_gui_func, font=("Verdana", 14), bg="#FF6347", fg="white", relief="raised", bd=3)
    calculate_button.grid(row=5, column=1, columnspan=2, pady=20)

    # Tombol untuk reset form
    def clear_entries():
        fx_entry.delete(0, tk.END)
        lower_entry.delete(0, tk.END)
        upper_entry.delete(0, tk.END)

    reset_button = tk.Button(root, text="Reset", command=clear_entries, font=("Verdana", 14), bg="#00BFFF", fg="white", relief="raised", bd=3)
    reset_button.grid(row=6, column=1, columnspan=2, pady=10)

    # Jalankan aplikasi
    root.mainloop()

if __name__ == "__main__":
    main()
