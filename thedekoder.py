from cryptography.fernet import Fernet

def load_key():
    with open("key.txt", "rb") as file:
        return file.read()

def decode(encoded_password):
    key = load_key()
    f = Fernet(key)
    decoded_password = f.decrypt(encoded_password.encode())
    return decoded_password.decode()

print("Welcome to The Dekoder")
encoded_password = input("Enter the encoded text : ")
decoded_password = decode(encoded_password)
print(f"Decoded : {decoded_password}")
