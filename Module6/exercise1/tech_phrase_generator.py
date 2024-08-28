import requests
import json

api_url = "https://techy-api.vercel.app/api/json"
response = requests.get(api_url)
json_data = response.text

techy_data = json.loads(json_data)

print(f"Tech Phrase: {techy_data["message"]}")