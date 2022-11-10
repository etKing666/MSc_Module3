import base64
from cmd import Cmd

class Prompt(Cmd):
    def do_encrypt(self, inp):
        """Prompts for the text for encryption."""
        text = input("Enter the text that you want to encrypt:")
        bytes_text = text.encode('ascii')  # base64 accepts bytes-like data, so we convert string to bytes
        encrypted_text = base64.b64encode(bytes_text)  # base64 encrypts the data
        final_text = encrypted_text.decode('ascii')  # We convert the encrypted data back to human-readable format
        print(f"The encrypted text is: {final_text}")
        return

    def do_decrypt(self, inp):
        """Prompts for the text for decryption."""
        text = input("Enter the text that you want to decrypt:")
        bytes_text = text.encode('ascii')
        decrypted_text = base64.b64decode(bytes_text)
        final_text = decrypted_text.decode('ascii')
        print(f"The decrypted text is: {final_text}")
        return

    def do_exit(self, inp):
        """Exists the shell"""
        print("Thanks for using the shell. Bye!")
        return True  # Returns true so that Cmd.postcmd() hook method can terminate the execution.

    def newkeys(keysize):
       random_generator = Random.new().read
       key = RSA.generate(keysize, random_generator)
       private, public = key, key.publickey()
       return public, private

Prompt().cmdloop()
