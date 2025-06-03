import requests
import json
import os

API_BASE = "https://api.myanimelist.net/v2"
CLIENT_ID = os.getenv("client_id")

if not CLIENT_ID:
    raise EnvironmentError("Missing environment variable: client_id")

response = requests.get(
    f"{API_BASE}/anime",
    headers={"X-MAL-CLIENT-ID": CLIENT_ID},
    params={"q": "one", "limit": 4}
)

anime_list = response.json()

data = anime_list.get("data", [])

for item in data:
    node = item.get("node")
    if node:
        title = node.get("title")
        if title and title == "One Piece":
            print({"title": node.get("title")})