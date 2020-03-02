import base64


header = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
b64 = base64.b64decode(header)
print(b64)