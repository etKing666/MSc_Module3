import base64
from cryptography.fernet import Fernet
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from cmd import Cmd
from time import sleep


class Prompt(Cmd):
    def do_base64(self, inp):
        "Encrypt or decrypt using base64 algorithm"
        print("""
===================================
Base64 Encryption/Decryption Module
===================================
Commands:
encrypt - Encrypt a message using base64 algorithm
decrypt - Decrypt a message using base64 algorithm
exit - Return to main menu
        """)
        base64prompt().cmdloop()
        main()
        Prompt().cmdloop()


    def do_fernet(self, inp):
        "Encrypt or decrypt using fernet algorithm"
        print("""
===================================
Fernet Encryption/Decryption Module
===================================
Commands:
encrypt - Encrypt a message using fernet algorithm
decrypt - Decrypt a message using fernet algorithm
exit - Return to main menu
                """)
        fernetprompt().cmdloop()
        main()
        Prompt().cmdloop()

    def do_exit(self, inp):
        """Exists the shell"""
        print("Thanks for using the Encryption/Decryption Suite. Bye!")
        return True  # Returns true so that Cmd.postcmd() hook method can terminate the execution.

class base64prompt(Cmd):

    def do_encrypt(self, inp):
        """Prompts for the text for encryption. Simply enter the text that you'd like to encrypt."""
        text = input("Enter the text that you want to encrypt:")
        bytes_text = text.encode('ascii')  # base64 accepts bytes-like data, so we convert string to bytes
        encrypted_text = base64.b64encode(bytes_text)  # base64 encrypts the data
        final_text = encrypted_text.decode('ascii')  # We convert the encrypted data back to human-readable format
        print(f"The encrypted text is: {final_text}")
        return

    def do_decrypt(self, inp):
        """Prompts for the text for decryption. Simply enter the text that you'd like to decrypt."""
        text = input("Enter the text that you want to decrypt:")
        bytes_text = text.encode('ascii')
        decrypted_text = base64.b64decode(bytes_text)
        final_text = decrypted_text.decode('ascii')
        print(f"The decrypted text is: {final_text}")
        return

    def do_exit(self, inp):
        """Returns to main menu"""
        print("Returning to main menu...")
        sleep(1)
        return True

class fernetprompt(Cmd):

    def do_encrypt(self, inp):
        """
You are required to enter a text for encryption.
REMEMBER TO SAVE YOU FERNET KEY!
If you would like to decrypt your message later, you will be asked for your key. Otherwise, you will not be able to decrypt your message!
"""
        text = input("Enter the text that you want to encrypt:")
        key = Fernet.generate_key()
        print(f"""This is you key: {key.decode()}
Remember to store it in a safe place! You will need this key to decrypt your message later on.
""")
        f = Fernet(key)
        token = f.encrypt(text.encode("ascii"))
        print(f"""Here is the cipher text: {token.decode()}
        If you want to decrypt it later, you will need the cipher text and the key. 
        """)

    def do_decrypt(self, inp):
        """Decrypts a message with a key given by the user"""
        cipher = input("Enter the text that you want to decrypt:")
        key = input("Enter your key:")
        f = Fernet(key.encode("ascii"))
        message = f.decrypt(cipher.encode("ascii"))
        print(f"""
Here is the your decrypted message: {message.decode()}
""")

    def do_exit(self, inp):
        """Returns to main menu"""
        print("Returning to main menu...")
        sleep(1)
        return True

def main():
    print("""
    ===================================
    Encryption/Decryption Suite
    ===================================
    Commands:
    base64 - Encrypt or decrypt a message using base64 algorithm
    fernet - Encrypt or decrypt a message using fernet algorithm
    help - Get help and review the documentation of a command
    exit - Exits the program
            """)

main()
Prompt().cmdloop()
