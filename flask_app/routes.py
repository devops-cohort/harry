'''Python file that handles hyperlink routing within the site'''
from flask import render_template, redirect, url_for, request
from flask_app import app, db, bcrypt
from flask_app.models import Constellations, Users
from flask_app.forms import ConstellationForm, SignUpForm, LogInForm
from flask_login import login_user, current_user, logout_user, login_required

# Route to login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
	
    # Define a form to allow user to log in
    form = LogInForm()
	
    if form.validate_on_submit():
        user = Users.query.filter_by(user_name=form.user_name.data).first()
	
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            next_page = request.args.get('next')

            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))

    return render_template('login.html', title='Login', form = form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

# Route to sign up page
@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    # Define a form to allow user to sign up
    form = SignUpForm()

    if form.validate_on_submit():
        # Hash Pasword
        hashed_pw = bcrypt.generate_password_hash(form.password.data)
        user = Users(user_name = form.user_name.data,
	    email = form.email.data,
            password = hashed_pw)
        # Send data to database
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        print(form.errors)

    return render_template('signup.html', title='Sign Up', form = form)

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

'''
# Route to celestial database
@app.route('/lookup')
@app.route('/query')
def query():
    return render_template('query.html', title='Look Up')
'''

# Route to observation post page
@app.route('/enterconstellation', methods = ['GET', 'POST'])
@login_required
def enter_constellation():
    form = ConstellationForm()

    if form.validate_on_submit():
        constellation_data = Constellations(
            name = form.name.data,
            right_ascension = form.right_ascension.data,
            declination = form.declination.data,
            asterism = form.asterism.data,
            description = form.description.data
        )

        db.session.add(constellation_data)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        print(form.errors)

    return render_template('enterconstellation.html', title = 'Enter Constellation', form = form)
