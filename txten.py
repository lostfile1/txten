import base64
import sys
import os

if sys.argv[2] == "en":
  print(base64.b64encode(sys.argv[1]))
  
  if sys.argv[2] == "dc": 
    print(base64.b64decode(sys.argv[1]))



