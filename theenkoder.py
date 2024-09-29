from cryptography.fernet import Fernet

# Génère une clé et l'enregistre dans un fichier
def keygen():
    key = Fernet.generate_key()
    with open("key.txt", "wb") as file:
        file.write(key)

# Lit la clé depuis le fichier
def load_key():
    with open("key.txt", "rb") as file:
        return file.read()

# Encode le mot de passe en utilisant la clé
def encode(password):
    key = load_key()  # Charger la clé
    f = Fernet(key)   # Créer une instance Fernet avec la clé
    encoded_password = f.encrypt(password.encode())  # Chiffrer le mot de passe
    return encoded_password.decode()  # Retourner le mot de passe encodé en chaîne de caractères



print("Welcome to The Enkoder")
print("If you have a key, place the key.txt in the .py folder and enter A")
print("If you don't, press O and we'll generate a key.txt for you that you can use to decode.")
choice = input("Your choice : ")

if choice == "A":
    password = input("Enter the text to encode: ")
    encoded_password = encode(password)  # Encode le mot de passe
    print(f"Encoded text : {encoded_password}")

elif choice == "O":
    password = input("Enter the text to encode: ")
    keygen()  # Génère une clé
    encoded_password = encode(password)  # Encode le mot de passe
    print(f"Encoded text : {encoded_password}")
