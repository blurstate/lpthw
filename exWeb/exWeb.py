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
        
        cityStores = []
        allStores = storelists.Store.getAll(city=city)
        # for s in allStores:
        #     if s.city == city:
        #         cityStores.append(s)
                
        return render.index(stores=allStores, myCity=city)    
    
    def GET(self):

        allStores = storelists.Store.getAll()
        
        return render.index(stores=allStores, myCity='')
        
if __name__ == '__main__':
    app.run()