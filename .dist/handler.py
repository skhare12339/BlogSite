import tornado.web
import sqlite3

conn = sqlite3.connect('C:\Users\Sanjay-pc\Desktop\edugorilla\databse\data.db')
c = conn.cursor()

try:
    c.execute('''CREATE TABLE users (Name_of_publisher text, Topic_name text, Post text)''')
except sqlite3.OperationalError:
    pass


class BaseHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index1.html')


class Saver(tornado.web.RequestHandler):
    def post(self):
        Name_of_publisher = self.get_argument('Name_of_publisher')
        Topic_name = self.get_argument('Topic_name')
        Post = self.get_argument('Post')
        c.execute("insert into users values (?, ?, ?)", (Name_of_publisher, Topic_name, Post))
        conn.commit()
        self.redirect('/success')

class Getter(tornado.web.RequestHandler):
    def get(self):
        c.execute('select * from users')
        res = c.fetchall()
        
        resultant = []
        for i in res:
            resultant.append(i)
        self.write(str(resultant))