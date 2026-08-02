import requests

url = "https://ksp.co.il/web/cat/1215?search=%D7%A7%D7%9C%D7%A4%D7%99%20%D7%A4%D7%95%D7%A7%D7%99%D7%9E%D7%95%D7%9F"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120 Safari/537.36"
}

response = requests.get(url, headers=headers)

print("Status:", response.status_code)

print(response.text[:500])
