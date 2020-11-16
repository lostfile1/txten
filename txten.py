import os
import sys
import base64


if sys.argv[2] == 'en':
  encoded = base64.b64encode(sys.argv[1])
  print(encoded)

elif sys.argv[2] == 'de':
  data = base64.b64decode(sys.argv[1])
  print(data)

elif sys.argv[2] == 'credit':
  print('script made by whitepaperkat')
  print('donate : bc1qyvrvxygaw4dqmwu3sg0gsl79uwyh6u2p99vcr2\n')
else:
  print('im sorry but i cant do that dave')
