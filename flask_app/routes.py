'''Python file that handles hyperlink routing within the site'''
from flask import render_template, redirect, url_for, request
from flask_app import app, db, bcrypt
from flask_app.models import Observations, Users
from flask_app.forms import ObservationForm, SignUpForm, LogInForm, UpdateAccountForm, DeleteAccount
from flask_login import login_user, current_user, logout_user, login_required

# Route to login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    # If user navigates to this page when logged in, redirect to home page
    if current_user.is_authenticated:
        return redirect(url_for('home'))
	
    # Define a form to allow user to log in
    form = LogInForm()
	
    # If the form passes validation checks
    if form.validate_on_submit():
        # Query the database for users with the username passed through the form
        user = Users.query.filter_by(user_name=form.user_name.data).first()
        # If user exists and form password == hashed password in database
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # Log the user in using these details
            login_user(user, remember = form.remember.data)
            # Set page to redirect to as the page the user was trying to navigate to
            next_page = request.args.get('next')

            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
        else:
            print(form.errors)
    else:
        print(form.errors)

    return render_template('login.html', title='Login', form = form)

# Route logs the currently logged-in user out
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

# Route to sign up page
@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    # If user navigates to this page when logged in, redirect to home page
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    # Define a form to allow user to sign up
    form = SignUpForm()

    if form.validate_on_submit():
        # Hash Pasword
        hashed_pw = bcrypt.generate_password_hash(form.password.data)
        user = Users(
            user_name = form.user_name.data,
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            email = form.email.data,
            password = hashed_pw
        )
        # Send data to database
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    else:
        print(form.errors)

    return render_template('signup.html', title='Sign Up', form = form)

# Route to home page
@app.route('/')
@app.route('/home')
def home():
    # Query database for all observations,
    # order by date/time posted in descending order
    observations = Observations.query.order_by(Observations.post_date_time.desc()).all()
    return render_template('home.html', title = 'Home', posts = observations)

# Route to about page
@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    # Create account update form
    form = UpdateAccountForm()
    # Create delete button
    delete_account = DeleteAccount()
    
    # If update form passes validation upon submit
    if form.validate_on_submit():
        current_user.user_name = form.user_name.data
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('account'))
    # Else if the the http request is a GET request
    elif request.method == 'GET':
        form.user_name.data = current_user.user_name
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
   
    # If the delete button is pressed
    if delete_account.is_submitted():
        user = Users.query.filter_by(userID = current_user.userID).first()
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('signup'))

    return render_template('account.html', title = 'Account', form = form, delete = delete_account)

# Route to observation post page
@app.route('/enterobservation', methods = ['GET', 'POST'])
@login_required
def enter_observation():
    # Define the form
    form = ObservationForm()
    # If the form passes validation
    if form.validate_on_submit():
        observation_data = Observations(
            title = form.title.data,
            author = current_user,
            location = form.location.data,
            azimuth = form.azimuth.data,
            altitude = form.altitude.data,
            description = form.description.data
        )

        # Create an association with the observers and the observation
        observation_data.observers.append(current_user)
        if form.observer1.data != '':
            observer1 = Users.query.filter_by(user_name = form.observer1.data).first()
            if observer1:
                observation_data.observers.append(observer1)
        if form.observer2.data != '':
            observer2 = Users.query.filter_by(user_name = form.observer2.data).first()
            if observer2:
                observation_data.observers.append(observer2)

        # Add these changes to the database
        db.session.add(observation_data)
        # Commit        
        db.session.commit()
        return redirect(url_for('home'))
    else:
        print(form.errors)

    return render_template('enterobservation.html', title = 'Enter Observation', form = form) 

# Route to coverage report page
@app.route('/coverage')
def coverage_report():
    return render_template('coveragereport.html', title = 'Coverage Report')
