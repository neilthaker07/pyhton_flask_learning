from flask import Flask, request, render_template

app = Flask(__name__)  # root main beacuse of __name__ for flask
'''
# mapping URL to python function, decorator
@app.route('/') # connect a webpage,  / is root dir - home page of website    REST ENDPOINT
def index():   # same as webpage - here / 
	return 'This is home' + request.method       # GET from request method
'''	
# multiple URL
@app.route('/')
@app.route('/<user>')
def index(user=None):
	return render_template('user.html',user=user)
	
	
@app.route('/tune')	
def tune():
	return '<h2>It\'s Tune</h2>'
	
@app.route('/profile2/<username>')	  # var is defult string
def profile2(username):
	return 'Username in profile is : '+ username

@app.route('/post/<int:pid>')  # for int it must be specified
def post(pid):
	return 'Id is '+ str(pid)

@app.route('/handle', methods=['GET', 'POST'])  # GET is default
def handle():
	if request.method == 'POST':
		return 'POST IT IS'
	else:
		return 'GET IT IS'

# templates
@app.route('/profile/<name>')
def profile(name):
	return render_template('profile.html',name=name) # templates is a folder for what flask is looking for, static has css files

@app.route('/shopping')
def shopping():
	food = ['ad','ddfdfsa','nghm']
	return render_template('shopping.html', food=food	)

if __name__ == "__main__":   # only run if this file is run directly 
	app.run(debug=True) # start web server












