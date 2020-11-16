import base64
import sys




if sys.argv[2] == 'en':
  encodedBytes = base64.b64encode(sys.argv[1])
  print(encodedBytes)

elif sys.argv[2] == 'dc':
  decodedBytes = base64.b64decode(sys.argv[1])
  print(decodedBytes)   
