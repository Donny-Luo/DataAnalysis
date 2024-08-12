import requests
import json

response = requests.get('https://www.v2ex.com/api/topics/hot.json')
parsed_result = json.loads(response.text)
print(parsed_result)
