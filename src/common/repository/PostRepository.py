import csv

class PostRepository:  
    def __init__():
        with open('./database/posts.csv', newline='') as csvfile:
            postReader = csv.reader(csvfile, delimiter=',')
        
    def savePost(self, post):
        