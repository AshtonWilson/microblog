from app import app
print("routes.py loaded")



@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Ashton'}
    return render_template('index.html', title='Home', user=user)