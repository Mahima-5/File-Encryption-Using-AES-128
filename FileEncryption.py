from cryptography.fernet import Fernet
import os

# Function to generate a new key and save it
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("Encryption key generated and saved to 'key.key'.")

# Function to load the existing key
def load_key():
    if not os.path.exists("key.key"):
        print("Key file not found. Please generate a key first.")
        return None
    return open("key.key", "rb").read()

# Function to encrypt a file
def encrypt_file(filename):
    key = load_key()
    if key is None:
        return
    fernet = Fernet(key)
    
    try:
        with open(filename, "rb") as file:
            original = file.read()
        encrypted = fernet.encrypt(original)
        with open(filename, "wb") as encrypted_file:
            encrypted_file.write(encrypted)
        print(f"File '{filename}' encrypted successfully.")
    except FileNotFoundError:
        print("File not found. Please enter a valid file path.")

# Function to decrypt a file
def decrypt_file(filename):
    key = load_key()
    if key is None:
        return
    fernet = Fernet(key)
    
    try:
        with open(filename, "rb") as enc_file:
            encrypted = enc_file.read()
        decrypted = fernet.decrypt(encrypted)
        with open(filename, "wb") as dec_file:
            dec_file.write(decrypted)
        print(f"File '{filename}' decrypted successfully.")
    except FileNotFoundError:
        print("File not found. Please enter a valid file path.")
    except Exception as e:
        print("Decryption failed. Error:", e)

# CLI Menu
def main():
    while True:
        print("\n🔐 File Encryption System")
        print("1. Generate Key")
        print("2. Encrypt File")
        print("3. Decrypt File")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            generate_key()
        elif choice == '2':
            filepath = input("Enter the path of the file to encrypt: ").strip()
            encrypt_file(filepath)
        elif choice == '3':
            filepath = input("Enter the path of the file to decrypt: ").strip()
            decrypt_file(filepath)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
