import base64
from cryptography.fernet import Fernet
from cmd import Cmd


def do_base64encrypt(self, inp):
    """Prompts for the text for encryption. Simply enter the text that you'd like to encrypt."""
    text = input("Enter the text that you want to encrypt:")
    bytes_text = text.encode('ascii')  # base64 accepts bytes-like data, so we convert string to bytes
    encrypted_text = base64.b64encode(bytes_text)  # base64 encrypts the data
    final_text = encrypted_text.decode('ascii')  # We convert the encrypted data back to human-readable format
    print(f"The encrypted text is: {final_text}")
    return


def do_base64decrypt(self, inp):
    """Prompts for the text for decryption. Simply enter the text that you'd like to decrypt."""
    text = input("Enter the text that you want to decrypt:")
    bytes_text = text.encode('ascii')
    decrypted_text = base64.b64decode(bytes_text)
    final_text = decrypted_text.decode('ascii')
    print(f"The decrypted text is: {final_text}")
    return

def do_fernetencrypt(self, inp):
    """You are required to enter a text for eencryption.
    REMEMBER TO SAVE YOU FERNET KEY!
    If you would like to decrypt your message later, you will be asked for your key. Otherwise, you will not be able to decrypt your message!"""
    text = input ()
    key = Fernet.generate_key()
    print(key)
    f = Fernet(key)

def do_exit(self, inp):
    """Exists the shell"""
    print("Thanks for using the shell. Bye!")
    return True  # Returns true so that Cmd.postcmd() hook method can terminate the execution.

key = Fernet.generate_key()
print(key)
f = Fernet(key)
#token = f.encrypt(b"I am Etkin Getir.")
#print(token.decode())
#token2 = f.decrypt(b"gAAAAABjcMm9KrUGDgWbtPp7DfQeQJDROz4VKD-q6zpbQ7TQSS3AoFO95qYlx1WQeTLTc-kLUagHHOdL7upQd4Pj6sMJdfnP8i_sLrqS1RYXecyEO_zlt-U=")
#print(token2.decode())