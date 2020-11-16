import base64
import sys

if sys.argv[2] == 'en':
  pu = sys.argv[1].encode("ascii")
  data = base64.b64encode(pu)
  print(data)
 elif sys.argv[2] == 'dc':
   data = base64.b64decode(sys.argv[1])
   print(data)



