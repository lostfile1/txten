import base64
import sys

if sys.argv[2] == "en":
  data = base64.b64encode(sys.argv[1])
  print(data)
  
  if sys.argv[2] == "dc": 
   data = base64.b64decode(sys.argv[1])
   print(data)



