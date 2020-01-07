import requests
print(requests.__version__)

google = requests.get("https://google.com")
print(google)