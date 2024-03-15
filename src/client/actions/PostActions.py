import json

class PostActions:
    def sendPostRequest(post, _socket):
        action = {"action": "createPost"}
        requestJson = json.dumps(action | post.__dict__)
        _socket.send(requestJson.encode('ascii'))