from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length

''' NOT IMPLEMENTED
# Class for logging in
class LogInForm(FlaskForm):
	user_name = StringField('User Name',
		validators = [
			DataRequired()
		])
	password = StringField('Password',
		validators = [
			DataRequired()
		])

# Class for signing up
class SignUpForm(FlaskForm):
	user_name = StringField('User Name',
		validators = [
			DataRequired(),
			Length(min = 3, 15)
		])
	passowrd = StringField('Password',
		validators = [
			DataRequired(),
			Length(min = 6, 30)
		])

# Class for observation post form
class ObservationForm(FlaskForm):
	title = StringField('Title',
		validators = [
			DataRequired(),
			Length(min = 1, max = 30)
		])
	star = StringField('Star',
		validators = [
			DataRequired(),
			Length(min = 1, max = 30)
		])
	date_time = DateTimeField('Date/Time',
		validators = [
			DataRequired(),
			Length(min = 1, max = 100)
		])
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

# Class for star post form
class StarForm(FlaskForm):
	name = StringField('Name',
		validators = [
			DataRequired(),
			Length(min = 1, max = 30)
		])
	constellation = StringField('Constellation',
		validators = [
			DataRequired(),
			Length(min = 1, max = 30)
		])
	right_ascension = StringField('Right Ascension',
		validators = [
			DataRequired(),
			Length(min = 1, max = 30)
		])
	declination = StringField('Declination',
		validators = [
			DataRequired(),
			Length(min = 1, max = 30)
		])
	description = StringField('Description',
		validators = [
				Length(min = 1, max = 2000)
		])
	submit = SubmitField('Submit')
'''

# Class for constellation post form
class ConstellationForm(FlaskForm):
	name = StringField('Name',
		validators = [
			DataRequired(),
			Length(min = 1, max = 30)
		])
	right_ascension = StringField('Right Ascension',
		validators = [
			DataRequired(),
			Length(min = 1, max = 30)
		])
	declination = StringField('Declination',
		validators = [
			DataRequired(),
			Length(min = 1, max = 100)
		])
	asterism = StringField('Asterism',
		validators = [
			Length(min = 0, max = 50)
		])
	description = StringField('Description',
		validators = [
			Length(min = 0, max = 2000)
		])
	submit = SubmitField('Submit')
