import base64
import sys


foo = sys.argv[1]
goo = sys.argv[2]

if goo == 'en':
  encodedBytes = base64.b64encode(foo.encode("utf-8"))
  encodedStr = str(encodedBytes, "utf-8")
  print(encodedStr)

elif goo == 'dc':
  decodedBytes = base64.b64decode(Sttr)
  decodedStr = str(decodedBytes, "utf-8")
  print(decodedStr)   
