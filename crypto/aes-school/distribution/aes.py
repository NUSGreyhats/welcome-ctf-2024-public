from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

with open("flag.txt", "r") as f:
    flag = f.read()

key = os.urandom(16)

def encrypt(message):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_message = pad(message, 16)
    ciphertext = cipher.encrypt(padded_message)
    return ciphertext

def decrypt(ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    try:
        padded_message = cipher.decrypt(ciphertext)
        message = unpad(padded_message, 16)
        return message
    except:
        return b""

menu = """
Enter an option:
[1] Encrypt
[2] Decrypt
[3] Exit
> """

def main():

    while True:
        option = input(menu).strip()

        if option == "1":

            msg = bytes.fromhex(input("Enter message to encrypt (hex): "))
            
            if b"gimme the flag!!" in msg:
                print("No.")
            else:
                print(f"Encrypted message: {encrypt(msg).hex()}")
                        
        elif option == "2":

            msg = bytes.fromhex(input("Enter encrypted message (hex): "))
            
            decrypted_msg = decrypt(msg)

            if b"gimme the flag!!" in decrypted_msg:
                print(f"Wow! Here's the flag: {flag}")
                exit(0)
                
            else:
                print(f"Decrypted message: {decrypted_msg.hex()}")
                
        else:
            exit(0)

if __name__ == "__main__":
    main()
