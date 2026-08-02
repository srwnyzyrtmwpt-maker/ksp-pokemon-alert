import requests

url = "https://ksp.co.il/web/cat/1215?search=%D7%A7%D7%9C%D7%A4%D7%99%20%D7%A4%D7%95%D7%A7%D7%99%D7%9E%D7%95%D7%9F"

response = requests.get(url)

print("Status:", response.status_code)

if "Pokemon" in response.text or "פוקימון" in response.text:
    print("מצאתי מוצרי פוקימון!")
else:
    print("לא נמצא פוקימון")
