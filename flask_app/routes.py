'''Python file that handles hyperlink routing within the site'''
from flask import render_template, redirect, url_for
from  flask_app import app, db
from flask_app.models import Constellations
import flask_app.forms

''' NOT IMPLEMENTED
# Route to login page
@app.route('/login')
@app.route('/signin')
def login():
	# Define a form to allow user to log in
	form = LogInForm()
	# If the form passes validation:
	if form.validate_on_submit():
		# Create an object based on the Users model (is this the best approach??)
		loginData = Users(
			user_name = form.user_name.data,
			password = form.last_name.data
		)
		# Query database for user name matching that in the form
		# NEEDS SOME KIND OF CONDITIONAL FOR IF THE USERNAME IS NOT FOUND
		user_data = session.query(Users).filter(Users.user_name == loginData.user_name).all()
		# Checks is password in form matches password in database for that user
		# If so, directs user to home page
		if user_data.password == loginData.password:
			return redirect(url_for('home'))
		else:
			print(form.errors)
	# Else, throw an error to the user
	else:
		print(form.errors)

	return render_template('login.html', title='Login')

# Route to sign up page
@app.route('/signup')
@app.route('/register')
def signup():
	# Define a form to allow user to sign up
	form = SignUpForm()
	
	if form.validate_on_submit():
		loginData = Users(
			user_name = form.user_name.data,
			password = form.last_name.data
		)
		
		# Send data to database
		db.session.add(loginData)
		db.session.commit()
		return redirect(url_for('login'))
	else:
		print(form.errors)

	return render_template('signup.html', title='Sign Up')
'''

# Route to home page
@app.route('/')
@app.route('/home')
def home():
	# Needs code here to redirect user to login page if they are not logged in
	# I think this redirect needs to be extended to each route
	constellation_data = Constellations.query.all()
	return render_template('home.html', title='Home', post = constellation_data)

# Route to about page
@app.route('/about')
def about():
	return render_template('about.html', title='About')

'''NOT IMPLEMENTED
# Route to sign out page
@app.route('/signout')
def signout():
	# Should redirect back to login page
	# Possible this needn't be a page in its own right, might just be a link that logs you out
	return render_template('signout.html', title='Sign Out')

# Route to celestial database
@app.route('/lookup')
@app.route('/query')
def query():
	return render_template('query.html', title='Look Up')
'''

# Route to observation post page
@app.route('/enterconstellation', methods = ['GET', 'POST'])
def enter_constellation():
	form = ConstellationForm()
	
	if form.validate_on_submit():
		constellation_data = Constellations(
			name = form.name.data,
			right_ascension = form.last_name.data,
			declination = form.title.data,
			asterism = form.content.data,
			description = form.description.data
		)
		
		db.session.add(constellation_data)
		db.session.commit()
		return redirect(url_for('home'))
	else:
		print(form.errors)

	return render_template('enterconstellation.html', title = 'Enter Constellation', form = form)
