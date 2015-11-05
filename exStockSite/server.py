import web

urls = (
'/', 'Index',
'/stock/(.+)', 'Stock',
)

app = web.application(urls, globals())
render = web.template.render('templates/')

class News(object):
    def __init__(self, url, headline):
        self.url = url
        self.headline = headline

class Index:
    def GET(self):
        
        f = [
            {'ticker':'AAPL', 'company':'Apple', 'change': '+1.5%'},
        ]
        
        n = [
            News('http://google.com', 'Google wins!!'), 
            News('http://yahoo.com', 'Yahoo loses.'),
        ]
        return render.index(favorites=f, news=n)   
        
if __name__ == '__main__':
    app.run()