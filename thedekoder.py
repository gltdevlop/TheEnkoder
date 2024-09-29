from cryptography.fernet import Fernet
import os

def load_key():
    with open("key.txt", "rb") as file:
        return file.read()

def decode(encoded_password):
    key = load_key()
    f = Fernet(key)
    decoded_password = f.decrypt(encoded_password.encode())
    return decoded_password.decode()

print("Welcome to The Dekoder")
print("Please place the key you used to encode your text in the same folder that thedekoder.py is.")

if (os.path.isfile("key.txt")):
    encoded_password = input("Enter the encoded text : ")
    decoded_password = decode(encoded_password)
    print(f"Decoded : {decoded_password}")
else:
    print("Key not present. Please restart the software and place the key to decode.")
    quit()

