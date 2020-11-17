import os
import sys
import base64


if sys.argv[2] == 'en':
  print(base64.b64encode(sys.argv[1]))

elif sys.argv[2] == 'de': 
  print(base64.b64decode(sys.argv[1]))

elif sys.argv[2] == 'credit':
  print('script made by whitepaperkat')
  print('donate : bc1qyvrvxygaw4dqmwu3sg0gsl79uwyh6u2p99vcr2\n')
