import base64
import sys




if sys.argv[2] == 'en':
  encodedBytes = base64.b64encode(sys.argv[1].encode("utf-8"))
  encodedStr = str(encodedBytes, "utf-8")
  print(encodedStr)

elif sys.argv[2] == 'dc':
  decodedBytes = base64.b64decode(Sttr)
  decodedStr = str(decodedBytes, "utf-8")
  print(decodedStr)   
