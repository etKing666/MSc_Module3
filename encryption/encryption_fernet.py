from cryptography.fernet import Fernet

text = input("Enter a message for encryption: ")
key = Fernet.generate_key()  # Key is generared. We need this key for decryption as well.
f = Fernet(key)
token = f.encrypt(text.encode("ascii"))  # We use encode method to covert it to a bytes-like input.
print(f"Your encrypted message is: {token.decode()}")  # We decode it back to human-readble format
plain = f.decrypt(token)
print(f"Your decrypted message is: {plain.decode()}")