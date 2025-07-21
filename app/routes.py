from app import app
print("routes.py loaded")



@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Ashton'}
    return f"""
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, {user['username']}!</h1>
    </body>
</html>"""