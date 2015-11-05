import web
import storelists

urls = (
'/', 'index',
'/hogs', 'razorback',
)

app = web.application(urls, globals())
render = web.template.render('templates/')

class razorback:
    def GET(self):
        html = """
            <html>
                <head></head>
                <body>
                    <h1>Beat Bama!</h1>
                </body>
            </html>
        """
        return html

class index:
    def POST(self):
        form = web.input(myCity="")
        city = form.myCity
        
        allStores = storelists.Store.getAll(city=city)
                
        return render.index(stores=allStores, myCity=city)    
    
    def GET(self):

        allStores = storelists.Store.getAll()
        
        return render.index(stores=allStores, myCity='')
        
if __name__ == '__main__':
    app.run()