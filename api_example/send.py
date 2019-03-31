from pprint import pprint

import requests


headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTU0MDI1ODU0LCJqdGkiOiI2ODk4OWVlZGY4NzI0ZGU2OGYzYTAzMDUzNTRjYmM0ZCIsInVzZXJfaWQiOjF9.vWPzMCKzsB9q9HxE5jNLNlKKtLRkpkgqPtcuo2KUEHY'
r = requests.get('http://127.0.0.1:8000/paradigms/', headers=headers)

pprint(r.text)