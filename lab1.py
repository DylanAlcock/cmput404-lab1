import requests
print(requests.__version__)

google = requests.get("https://google.com")
print(google)

var = requests.get("https://raw.githubusercontent.com/DylanAlcock/cmput404-lab1/master/lab1.py")
print(var.content)