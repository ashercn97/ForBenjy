import requests

url = 'http://127.0.0.1:5000/api/send'  # Replace with the correct URL if needed
files = {'file': open('./yay.png', 'rb')}  # Replace with your file path

response = requests.post(url, files=files)
print(response.json())
