import json

data = json.dumps({"username": "ricardo"}).encode("ascii")
data = json.loads(data.decode("ascii"))
data["username"] = data["username"].upper()
data = json.dumps(data)