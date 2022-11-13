from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt():
    from Crypto.Cipher import AES
    text = input("Enter the text that you want to encrypt:")
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(text.encode("ascii"))
    print(f"Here is your cipher text: {ciphertext.decode('latin-1')}")
    print(f"Here is your key: {key.decode('latin-1')}")
    print(f"Here is your nonce: {nonce.decode('latin-1')}")
    print(f"Here is your tag: {tag.decode('latin-1')}")

def decrypt():
    ciphertext = input("Enter the text that you want to decrypt:")
    key = input("Enter your key:")
    nonce = ("Enter your nonce:")
    tag = ("Enter your tag:")
    cipher = AES.new(key.encode("latin-1"), AES.MODE_EAX, nonce=nonce.encode("latin-1"))
    plaintext = cipher.decrypt(ciphertext.encode("latin-1"))
    try:
        cipher.verify(tag.encode("latin-1"))
        print("The message is authentic:", plaintext.decode())
    except ValueError:
        print("Key incorrect or message corrupted")

encrypt()
decrypt()
