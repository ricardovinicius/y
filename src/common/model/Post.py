import sqlite3

'''
    PostJson structure:
'''


class Post:
    def __init__(self, id, title, body, likes, date, time, username):
        self.id = id
        self.title = title
        self.body = body
        self.likes = likes
        self.date = date
        self.time = time
        self.username = username
    
    def _initTable():
        dbConn = sqlite3.connect("resources/database.db")
        cur = dbConn.cursor()
        
        cur.execute("CREATE TABLE posts(id, )")
        
    
    
            