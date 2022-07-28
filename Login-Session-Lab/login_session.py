from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'



@app.route('/', methods = ['GET', 'POST']) # What methods are needed?
def home():
	if request.method == 'GET':
		return render_template('home.html')
	else:
		name = request.form['name_ofAuthor']
		age = request.form['Age']
		message = request.form['message']

		if age.isdigit():
			login_session['Author'] = name
			login_session['age'] = age
			login_session['message'] = message
			return render_template('thanks.html')
		else:
			return render_template('error.html')






	
	


@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():

	return render_template('display.html', name = login_session['Author'], age = login_session['age'],
	message = login_session['message'], login_session = login_session) # What variables are needed?


@app.route('/thanks', methods=['GET', 'FORM'])
def thanks():

	return render_template('home.html')




if __name__ == '__main__':
	app.run(debug=True)