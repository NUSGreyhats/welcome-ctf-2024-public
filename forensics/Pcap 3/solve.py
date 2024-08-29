import pandas as pd
from base64 import b64decode

df = pd.read_csv('filtered.csv')

# Get Info column
info = df['Info']

msg = ""
for i in info:
    query = i.split(" ")[4]
    exfil = query.replace(".welc0mectf.gr3yh4ts.com", "")
    msg += exfil

print(b64decode(msg))