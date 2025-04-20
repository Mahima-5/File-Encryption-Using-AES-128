from cryptography.fernet import Fernet
import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to generate a new key and save it
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    status_label.config(text="🔑 Key generated and saved to 'key.key'")

# Function to load the existing key
def load_key():
    if not os.path.exists("key.key"):
        messagebox.showerror("Error", "Key file not found. Generate a key first.")
        return None
    return open("key.key", "rb").read()

# Function to encrypt a file
def encrypt_file():
    key = load_key()
    if key is None:
        return
    fernet = Fernet(key)
    filepath = filedialog.askopenfilename(title="Select File to Encrypt")
    if not filepath:
        return

    try:
        with open(filepath, "rb") as file:
            original = file.read()
        encrypted = fernet.encrypt(original)
        with open(filepath, "wb") as encrypted_file:
            encrypted_file.write(encrypted)
        status_label.config(text=f"🔒 File encrypted: {os.path.basename(filepath)}")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to decrypt a file
def decrypt_file():
    key = load_key()
    if key is None:
        return
    fernet = Fernet(key)
    filepath = filedialog.askopenfilename(title="Select File to Decrypt")
    if not filepath:
        return

    try:
        with open(filepath, "rb") as enc_file:
            encrypted = enc_file.read()
        decrypted = fernet.decrypt(encrypted)
        with open(filepath, "wb") as dec_file:
            dec_file.write(decrypted)
        status_label.config(text=f"🔓 File decrypted: {os.path.basename(filepath)}")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
    except Exception as e:
        messagebox.showerror("Decryption Failed", f"Error: {e}")

# GUI Setup
root = tk.Tk()
root.title("File Encryption System")
root.geometry("400x250")
root.resizable(False, False)

tk.Label(root, text="🔐 File Encryption System", font=("Arial", 16)).pack(pady=10)

tk.Button(root, text="Generate Key", command=generate_key, width=25).pack(pady=5)
tk.Button(root, text="Encrypt File", command=encrypt_file, width=25).pack(pady=5)
tk.Button(root, text="Decrypt File", command=decrypt_file, width=25).pack(pady=5)

status_label = tk.Label(root, text="", fg="blue")
status_label.pack(pady=10)

tk.Button(root, text="Exit", command=root.destroy, width=25).pack(pady=5)

root.mainloop()
