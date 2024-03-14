import json
import datetime as dt 

data = json.dumps({"username": "ricardo"}).encode("ascii")
data = json.loads(data.decode("ascii"))
data["username"] = data["username"].upper()
data = json.dumps(data)

print(f'{dt.datetime.now().hour}:{dt.datetime.now().minute}')
print(f'{dt.datetime.now().date()}')