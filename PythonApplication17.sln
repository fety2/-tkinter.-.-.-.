import tkinter as tk
from tkinter import scrolledtext, messagebox
import numpy as np
import scipy.linalg as la
from scipy.optimize import minimize
from scipy import integrate
import sqlite3

# ==================================================
# ПРАКТИЧНА РОБОТА 2 — СЛАР
# ==================================================
def practical_2():
    win = tk.Toplevel()
    win.title("ПР2 — СЛАР")
    win.geometry("750x500")

    output = scrolledtext.ScrolledText(win, width=90, height=25)
    output.pack(padx=10, pady=10)

    def calculate():
        output.delete(1.0, tk.END)

        A = np.array([
            [1.00,  0.47, -0.11,  0.55],
            [0.42,  1.00,  0.35,  0.17],
            [-0.25, 0.67,  1.00,  0.36],
            [0.54, -0.32, -0.74,  1.00]
        ])
        b = np.array([1.33, 1.29, 2.11, 0.10])

        x1 = la.solve(A, b)
        lu, piv = la.lu_factor(A)
        x2 = la.lu_solve((lu, piv), b)

        r1 = A @ x1 - b
        r2 = A @ x2 - b

        output.insert(tk.END, f"Матриця A:\n{A}\n\n")
        output.insert(tk.END, f"Вектор b:\n{b}\n\n")
        output.insert(tk.END, "Рішення:\n")
        output.insert(tk.END, f"solve(): {x1}\n")
        output.insert(tk.END, f"LU:      {x2}\n\n")
        output.insert(tk.END, "Залишки:\n")
        output.insert(tk.END, f"Ax-b (solve): {r1}\n")
        output.insert(tk.END, f"Ax-b (LU):    {r2}\n\n")
        output.insert(tk.END, f"Норма (solve): {la.norm(r1):.6e}\n")
        output.insert(tk.END, f"Норма (LU):    {la.norm(r2):.6e}\n")
        output.insert(tk.END, f"Число обумовленості: {np.linalg.cond(A):.4f}\n")

    tk.Button(win, text="Виконати", command=calculate).pack()
    tk.Button(win, text="У головне меню", command=win.destroy).pack(pady=5)


# ==================================================
# ПРАКТИЧНА РОБОТА 3 — МІНІМІЗАЦІЯ
# ==================================================
def practical_3():
    win = tk.Toplevel()
    win.title("ПР3 — Мінімізація")
    win.geometry("500x350")

    output = scrolledtext.ScrolledText(win, width=60, height=15)
    output.pack(padx=10, pady=10)

    def f(X):
        x1, x2 = X
        return (1 - x1)**2 + (2 - x2)**2

    def calculate():
        output.delete(1.0, tk.END)
        x0 = [0, 0]

        nm = minimize(f, x0, method="Nelder-Mead")
        bfgs = minimize(f, x0, method="BFGS")

        output.insert(tk.END, "Nelder–Mead:\n")
        output.insert(tk.END, f"x = {nm.x}\nf(x) = {nm.fun}\nітерації = {nm.nit}\n\n")
        output.insert(tk.END, "BFGS:\n")
        output.insert(tk.END, f"x = {bfgs.x}\nf(x) = {bfgs.fun}\nітерації = {bfgs.nit}\n")

    tk.Button(win, text="Знайти мінімум", command=calculate).pack()
    tk.Button(win, text="У головне меню", command=win.destroy).pack(pady=5)


# ==================================================
# ПРАКТИЧНА РОБОТА 4 — ФУНКЦІЯ (БЕЗ ГРАФІКА)
# ==================================================
def practical_4():
    win = tk.Toplevel()
    win.title("ПР4 — Обчислення функції")
    win.geometry("400x250")

    output = scrolledtext.ScrolledText(win, width=50, height=10)
    output.pack(padx=10, pady=10)

    def calculate():
        output.delete(1.0, tk.END)
        x = np.linspace(-1, 1, 5)
        y = x**5 + x**4 - x**3 / 3 + 2
        for xi, yi in zip(x, y):
            output.insert(tk.END, f"x = {xi:.2f}  f(x) = {yi:.4f}\n")

    tk.Button(win, text="Обчислити значення", command=calculate).pack()
    tk.Button(win, text="У головне меню", command=win.destroy).pack(pady=5)


# ==================================================
# ПРАКТИЧНА РОБОТА 5 — ІНТЕГРАЛ (БЕЗ ГРАФІКА)
# ==================================================
def practical_5():
    win = tk.Toplevel()
    win.title("ПР5 — Інтегрування")
    win.geometry("450x250")

    output = scrolledtext.ScrolledText(win, width=55, height=10)
    output.pack(padx=10, pady=10)

    def calculate():
        output.delete(1.0, tk.END)
        a, b = 1, 10
        f = lambda x: 1 / x**2

        I_quad, _ = integrate.quad(f, a, b)
        I_rom = integrate.romberg(f, a, b)
        I_an = (-1/b) - (-1/a)

        output.insert(tk.END, f"Аналітичне: {I_an}\n")
        output.insert(tk.END, f"Quad:       {I_quad}\n")
        output.insert(tk.END, f"Romberg:    {I_rom}\n")

    tk.Button(win, text="Обчислити інтеграл", command=calculate).pack()
    tk.Button(win, text="У головне меню", command=win.destroy).pack(pady=5)


# ==================================================
# ПРАКТИЧНА РОБОТА 6 — БД + АУДИТ
# ==================================================
def practical_6():
    win = tk.Toplevel()
    win.title("ПР6 — База даних")
    win.geometry("500x400")

    def init_db():
        conn = sqlite3.connect("audit.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        cur.execute("CREATE TABLE IF NOT EXISTS audit_log (id INTEGER PRIMARY KEY, action TEXT)")
        conn.commit()
        conn.close()

    def insert_user():
        name = name_entry.get()
        age = age_entry.get()
        if not name or not age:
            messagebox.showerror("Помилка", "Заповніть всі поля")
            return

        conn = sqlite3.connect("audit.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
        cur.execute("INSERT INTO audit_log (action) VALUES (?)", (f"Додано користувача {name}",))
        conn.commit()
        conn.close()
        messagebox.showinfo("OK", "Користувача додано")

    def show_log():
        log.delete(1.0, tk.END)
        conn = sqlite3.connect("audit.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM audit_log")
        for row in cur.fetchall():
            log.insert(tk.END, f"{row}\n")
        conn.close()

    init_db()

    tk.Label(win, text="Ім'я").pack()
    name_entry = tk.Entry(win)
    name_entry.pack()

    tk.Label(win, text="Вік").pack()
    age_entry = tk.Entry(win)
    age_entry.pack()

    tk.Button(win, text="Додати користувача", command=insert_user).pack(pady=5)
    tk.Button(win, text="Показати аудит", command=show_log).pack()

    log = scrolledtext.ScrolledText(win, width=55, height=10)
    log.pack(pady=5)

    tk.Button(win, text="У головне меню", command=win.destroy).pack()


# ==================================================
# ГОЛОВНЕ ВІКНО
# ==================================================
root = tk.Tk()
root.title("Практичні роботи 2–6 (Tkinter)")
root.geometry("300x350")

tk.Label(root, text="Оберіть практичну роботу", font=("Arial", 12)).pack(pady=10)

tk.Button(root, text="Практична робота 2", command=practical_2).pack(fill="x", padx=20, pady=3)
tk.Button(root, text="Практична робота 3", command=practical_3).pack(fill="x", padx=20, pady=3)
tk.Button(root, text="Практична робота 4", command=practical_4).pack(fill="x", padx=20, pady=3)
tk.Button(root, text="Практична робота 5", command=practical_5).pack(fill="x", padx=20, pady=3)
tk.Button(root, text="Практична робота 6", command=practical_6).pack(fill="x", padx=20, pady=3)

tk.Button(root, text="Вийти", command=root.quit).pack(pady=10)

root.mainloop()


