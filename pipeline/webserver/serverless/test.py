import requests

# url = 'http://0.0.0.0:9696/predict'
url = 'http://127.0.0.1:8080/2015-03-31/functions/function/invocations'

# url = 'http://localhost:8080/2015-03-31/functions/function/invocations'
# url = 'https://m9vx7083f0.execute-api.ap-south-1.amazonaws.com/default/mlops-level-4/predict'

image_base64_str = '/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/wAALCAAcABwBAREA/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/9oACAEBAAA/APn+tzw34O1/xdPLFoemyXZiGZGDKirnplmIGfbNdOPgp4zjheW9t7CxVOv2m+iHHrkEj864/XtDuPD2pmwuri0nlCBy1pOsqDPbI7+1Zg5Ne5+OrbW/BvgPTNA8JWl22jyW32nUNYslLLcOww2WXOxfqRkEDsa8PlmlnkLzSPI/Tc7En9aZU1okEl5BHdTNDbtIollVNxRSeWA4zgc4r2Xwt4R+KOga3FBoOqBtGyrrem4V7N4j/GEJ547AZ6c9K5D4wTaDP8Qbp9AMLR+Wv2uS3/1b3GTvZeSP7ucd8/WuDoqxHf3kVs1tHdzpbt96JZCFP1GcVXor/9k='
payload = {
    "base64": image_base64_str,
}
print("URL @", url)
response = requests.post(url, json=payload)
print(response.json())

# assert response.json() == {
#     'duration': 0.0,
#     'model_version': '2f5413151de34a28941f3f0dfe028661',
# }
