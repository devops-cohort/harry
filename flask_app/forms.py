from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, FloatField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_app import db, bcrypt
from flask_app.models import Users
from flask_login import current_user

# Class for signing up
class SignUpForm(FlaskForm):
    user_name = StringField('User Name',
        validators = [
            DataRequired(),
            Length(min = 3, max = 15)
        ])
    first_name = StringField('First Name: ',
        validators = [
                DataRequired(),
                Length(min = 1, max = 50)
            ])
    last_name = StringField('Last Name: ',
        validators = [
                DataRequired(),
                Length(min = 1, max = 50)
            ])
    email = StringField('Email',
        validators = [
            DataRequired(),
                Email()
        ])
    password = PasswordField('Password',
        validators = [
            DataRequired()
        ])
    confirm_password = PasswordField('Confirm Password',
        validators = [
            DataRequired(),
            EqualTo('password')
        ])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email is already in use!')

class LogInForm(FlaskForm):
    user_name = StringField('User Name',
        validators = [
            DataRequired()
        ])
    password = PasswordField('Password',
        validators = [
            DataRequired()
	])

    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
    def validate_user(self, user_name):
        user = Users.query.filter_by(user=user_name.data).first()

        if user.user_name != user_name.data:
            raise ValidationError('User name not recognised')

    def validate_password(self, password):
        hashed_pw = bcrypt.generate_password_hash(password.data)
        user = Users.query.filter_by(password=password.data).first()

        if user.password != hashed_pw:
            raise ValidationError('Incorrect password')

# Class for account update form
class UpdateAccountForm(FlaskForm):
    user_name = StringField('User Name',
        validators = [
            DataRequired(),
            Length(min = 3, max = 15)
        ])
    first_name = StringField('First Name: ',
        validators = [
                DataRequired(),
                Length(min = 1, max = 50)
            ])
    last_name = StringField('Last Name: ',
        validators = [
                DataRequired(),
                Length(min = 1, max = 50)
            ])
    email = StringField('Email',
        validators = [
            DataRequired(),
                Email()
        ])
    submit = SubmitField('Update')
    
    def validate_email(self, email):
        if email.data != current_user.email:
            user = Users.query.filter_by(email = email.data).first()
            if user:
                raise ValidationError('Email already in use - Please choose another')

class DeleteAccount(FlaskForm):
    delete = SubmitField('Delete Account')

# Class for observation post form
class ObservationForm(FlaskForm):
    title = StringField('Title',
        validators = [
            DataRequired(),
            Length(min = 1, max = 30)
        ])
    observer1 = StringField('Observer 1')
    observer2 = StringField('Observer 2')
    location = StringField('Location',
        validators = [
            DataRequired(),
            Length(min = 1, max = 100)
        ])
    azimuth = FloatField('Azimuth',
        validators = [
            DataRequired()
        ])
    altitude = FloatField('Altitude',
        validators = [
            DataRequired()
        ])
    description = StringField('Description',
        validators = [
            Length(min = 1, max = 2000)
        ])
    submit = SubmitField('Submit')

    def validate_observer_1(self, observer1):
        exists = db.session.query(db.exists().where(Users.user_name == observer1.data)).scalar()

        if exists is False:
            raise ValidationError('User name not recognised')

    def validate_observer_2(self, observer2):
        exists = db.session.query(db.exists().where(Users.user_name == observer2.data)).scalar()

        if exists is False:
            raise ValidationError('User name not recognised')
