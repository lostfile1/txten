import base64

print("txtend v1.0")
print("this is a basic txt encoder made in python")

foo = input("type your message:")

encodedBytes = base64.b64encode(foo.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")

print(encodedStr)

