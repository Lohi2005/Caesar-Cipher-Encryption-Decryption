import tkinter as tk
from tkinter import messagebox

# ---------------- Caesar Cipher Functions ---------------- #
def encrypt(text, shift):
    """Encrypts the text using Caesar Cipher algorithm."""
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(text, shift):
    """Decrypts the text by reversing the Caesar Cipher algorithm."""
    return encrypt(text, -shift)

# ---------------- GUI Event Functions ---------------- #
def do_encrypt():
    text = entry_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Please enter a message!")
        return
    try:
        shift = int(entry_shift.get())
        if not (1 <= shift <= 25):
            raise ValueError
        encrypted = encrypt(text, shift)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, encrypted)
        label_output.config(text="🔐 Encrypted Message:")
        status_label.config(text="✅ Text successfully encrypted", fg="lightgreen")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid shift number (1–25)!")

def do_decrypt():
    text = entry_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Please enter a message!")
        return
    try:
        shift = int(entry_shift.get())
        if not (1 <= shift <= 25):
            raise ValueError
        decrypted = decrypt(text, shift)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, decrypted)
        label_output.config(text="🔓 Decrypted Message:")
        status_label.config(text="✅ Text successfully decrypted", fg="cyan")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid shift number (1–25)!")

# ---------------- GUI Setup ---------------- #
root = tk.Tk()
root.title("Caesar Cipher Program")
root.geometry("500x470")
root.config(bg="#1e1e2e")  # Dark background color

# Title Label
title_label = tk.Label(root, text="Caesar Cipher", font=("Arial", 18, "bold"), bg="#1e1e2e", fg="white")
title_label.pack(pady=10)

# Input Text
label_text = tk.Label(root, text="Enter your message:", bg="#1e1e2e", fg="white")
label_text.pack()
entry_text = tk.Text(root, height=5, width=50, bg="#2e2e3e", fg="white", insertbackground="white")
entry_text.pack(pady=5)

# Shift Value
label_shift = tk.Label(root, text="Enter shift value (1–25):", bg="#1e1e2e", fg="white")
label_shift.pack()
entry_shift = tk.Entry(root, bg="#2e2e3e", fg="white", insertbackground="white")
entry_shift.pack(pady=5)

# Buttons
btn_encrypt = tk.Button(root, text="Encrypt", command=do_encrypt, bg="#4CAF50", fg="white", width=15)
btn_encrypt.pack(pady=5)

btn_decrypt = tk.Button(root, text="Decrypt", command=do_decrypt, bg="#f44336", fg="white", width=15)
btn_decrypt.pack(pady=5)

# Output Text
label_output = tk.Label(root, text="Output:", bg="#1e1e2e", fg="white")
label_output.pack()
output_text = tk.Text(root, height=5, width=50, bg="#2e2e3e", fg="white", insertbackground="white")
output_text.pack(pady=5)

# Status Label
status_label = tk.Label(root, text="", bg="#1e1e2e", fg="white", font=("Arial", 10, "italic"))
status_label.pack(pady=5)

# Run the GUI
root.mainloop()
