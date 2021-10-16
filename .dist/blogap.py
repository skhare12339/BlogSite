import tornado.web
import tornado.ioloop


class mainpage(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello Noobs")

class htmlpage(tornado.web.RequestHandler):
    def get(self):
        self.render("index1.html")


if __name__ == "__main__":
    app=tornado.web.Application([
        (r"/",mainpage),
        (r"/html",htmlpage)

    ])


app.listen(8881)
print("I am   listening to 8881")
tornado.ioloop.IOLoop.current().start()