import base64
import sys

if sys.argv[2] == "en":
  pu = sys.argv[1].encode("ascii")
  data = base64.b64encode(pu)
  print(data)
 elif sys.argv[2] == "dc":
   pu = sys.argv[1].decode("ascii")
   data = base64.b64decode(pu)
   print(data)



