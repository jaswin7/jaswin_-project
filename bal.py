
import tkinter as tk
from tkinter import messagebox

username = "sheru"
pin = "1234"
balance = 5345000.00

root = tk.Tk()
root.title("My Bank")
root.geometry("400x450")
root.configure(bg="#f1f1f1")
root.resizable(False, False)

def update_balance():
    balance_label.config(text=f"₹ {balance:,.2f}")

def login():
    if user_entry.get() == username and pin_entry.get() == pin:
        login_frame.pack_forget()
        bank_frame.pack(fill="both", expand=True, padx=25, pady=15)
        update_balance()
        amount_entry.focus_set()
    else:
        messagebox.showerror("Login", "Incorrect username or PIN")
        pin_entry.delete(0, tk.END)
        pin_entry.focus_set()

def deposit():
    global balance
    try:
        amount = float(amount_entry.get())

        if amount <= 0:
            raise ValueError

        balance += amount
        update_balance()
        amount_entry.delete(0, tk.END)
        messagebox.showinfo("Bank", "Deposit successful")

    except ValueError:
        messagebox.showerror("Error", "Enter a valid amount")

def withdraw():
    global balance
    try:
        amount = float(amount_entry.get())

        if amount <= 0:
            raise ValueError

        if amount > balance:
            messagebox.showerror("Error", "Insufficient balance")
            return

        balance -= amount
        update_balance()
        amount_entry.delete(0, tk.END)
        messagebox.showinfo("Bank", "Withdrawal successful")

    except ValueError:
        messagebox.showerror("Error", "Enter a valid amount")

def logout():
    bank_frame.pack_forget()
    pin_entry.delete(0, tk.END)
    user_entry.delete(0, tk.END)
    login_frame.pack(pady=45)
    user_entry.focus_set()

def username_enter(event):
    pin_entry.focus_set()
    return "break"

def pin_enter(event):
    login()
    return "break"

def amount_enter(event):
    if selected_action.get() == "deposit":
        deposit()
    elif selected_action.get() == "withdraw":
        withdraw()
    else:
        messagebox.showwarning("Select Action", "Choose Deposit or Withdraw first")
    return "break"

# Heading
tk.Label(
    root, text="MY BANK",
    font=("Arial", 20, "bold"),
    bg="#f1f1f1", fg="#222222"
).pack(pady=20)

# Login screen
login_frame = tk.Frame(root, bg="#f1f1f1")
login_frame.pack(pady=45)

tk.Label(login_frame, text="Username",
         bg="#f1f1f1").pack(anchor="w")

user_entry = tk.Entry(login_frame, width=30)
user_entry.pack(pady=7)

tk.Label(login_frame, text="PIN",
         bg="#f1f1f1").pack(anchor="w")

pin_entry = tk.Entry(login_frame, width=30, show="*")
pin_entry.pack(pady=7)

tk.Button(
    login_frame, text="Login",
    width=25, command=login
).pack(pady=20)

# Keyboard navigation
user_entry.bind("<Return>", username_enter)
pin_entry.bind("<Return>", pin_enter)

# Banking screen
bank_frame = tk.Frame(root, bg="#f1f1f1")

tk.Label(
    bank_frame, text="Account Overview",
    font=("Arial", 15, "bold"),
    bg="#f1f1f1", fg="#222222"
).pack(anchor="w", pady=10)

tk.Label(
    bank_frame, text="Available Balance",
    bg="#f1f1f1", fg="#555555"
).pack(anchor="w")

balance_label = tk.Label(
    bank_frame, text="₹ 5000.00",
    font=("Arial", 24, "bold"),
    bg="#f1f1f1", fg="#222222"
)
balance_label.pack(anchor="w", pady=10)

tk.Label(
    bank_frame, text="Enter Amount (₹)",
    bg="#f1f1f1"
).pack(anchor="w", pady=5)

amount_entry = tk.Entry(bank_frame, width=30)
amount_entry.pack(anchor="w", pady=5)

# Select transaction
selected_action = tk.StringVar(value="")

tk.Radiobutton(
    bank_frame, text="Deposit",
    variable=selected_action, value="deposit",
    bg="#f1f1f1"
).pack(anchor="w")

tk.Radiobutton(
    bank_frame, text="Withdraw",
    variable=selected_action, value="withdraw",
    bg="#f1f1f1"
).pack(anchor="w")

tk.Button(
    bank_frame, text="Deposit",
    width=25, command=deposit
).pack(pady=8)

tk.Button(
    bank_frame, text="Withdraw",
    width=25, command=withdraw
).pack(pady=5)

tk.Button(
    bank_frame, text="Logout",
    width=25, command=logout
).pack(pady=20)

amount_entry.bind("<Return>", amount_enter)

# Initial focus
user_entry.focus_set()

root.mainloop()
t