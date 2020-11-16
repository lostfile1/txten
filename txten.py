import base64
import sys

if sys.argv[1] == 'en':
  data = base64.b64encode(sys.argv[2])
  print(data)
 
elif sys.argv[1] == 'dc':
   data = base64.b64decode(sys.argv[2])
   print(data)



