import jwt
import hashlib
import os
import requests
import uuid
from urllib.parse import urlencode, unquote

# access_key = os.environ['hYnFrBH2HdCuB9MxV0pNyT8tAeJ6sE5w5W3xqByo']
# secret_key = os.environ['DNAO12UvnXJ81B0cL8C8y6OYcRPRPTAtDelFDbQ4']
# server_url = os.environ['http.upbit.base-url']

access_key = 'hYnFrBH2HdCuB9MxV0pNyT8tAeJ6sE5w5W3xqByo'
secret_key = 'DNAO12UvnXJ81B0cL8C8y6OYcRPRPTAtDelFDbQ4'
server_url = 'https://api.upbit.com/'


payload = {
    'access_key': access_key,
    'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, secret_key)
authorization = 'Bearer {}'.format(jwt_token)
headers = {
  'Authorization': authorization,
}

res = requests.get(server_url + '/v1/accounts', headers=headers)
res.json()