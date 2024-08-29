from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

with open("flag.txt", "r") as f:
    flag = f.read()

assert(len(flag) == 31)

key = os.urandom(16)
iv = os.urandom(16)

def encrypt(message):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_message = pad(iv + message, 16)
    ciphertext = cipher.encrypt(padded_message)
    return ciphertext

def decrypt(ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    try:
        padded_message = cipher.decrypt(ciphertext)
        message = unpad(padded_message, 16)
        return True
    except:
        return False

menu = """
Enter an option:
[1] Encrypt flag
[2] Decrypt
[3] Exit
> """

def main():

    while True:
        option = input(menu).strip()

        if option == "1":

            print(f"Encrypted flag: {encrypt(flag.encode()).hex()}")
                        
        elif option == "2":

            msg = bytes.fromhex(input("Enter encrypted message (hex): "))
            
            if decrypt(msg):
                print("Message received!")
            else:
                print("Something wrong!")
                
        else:
            exit(0)

if __name__ == "__main__":
    main()
