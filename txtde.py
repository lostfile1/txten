import base64

print("this decodes messages")

encodedStr = input("encoded msg here :")

decodedBytes = base64.b64decode(encodedStr)
decodedStr = str(decodedBytes, "utf-8")

print(decodedStr)   

