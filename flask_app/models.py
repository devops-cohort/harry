'''Tables for the database are defined here'''
from flask_app import db, login_manager
from flask_login import UserMixin
from datetime import datetime

class Users(db.Model, UserMixin):
    # Table schema
    userID = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_name = db.Column(db.String(15), nullable = False, unique = True)
    email = db.Column(db.String(75), nullable = False, unique = True)
    password = db.Column(db.String(100), nullable = False)
    first_name = db.Column(db.String(50), nullable = False, unique = True)
    last_name = db.Column(db.String(50), nullable = False, unique = True)
    #constellations = db.relationship('Constellations', backref = 'User', lazy = True)
    observations = db.relationship('Observations', backref = 'author', lazy = True)

    def get_id(self):
        return self.userID

    def __repr__(self):
    	return ''.join([
            'User Name: ', self.user_name, '\r\n',
            'User ID: ', str(self.userID), '\r\n',
            'Email: ', self.email, '\r\n',
            'Name: ', self.first_name, ' ', self.last_name
	])

@login_manager.user_loader
def load_user(userID):
    return Users.query.get(int(userID))
'''
# Table to store constellation information
class Constellations(db.Model):
    #__name__ = 'constellation'
    constellationID = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(50), nullable = False)
    user = db.Column(db.Integer, ForeignKey('user.userID'), nullable = False)
    #num_stars = db.Column(db.Integer, nullable = False)
    right_ascension = db.Column(db.String(30), nullable = False)
    declination = db.Column(db.String(30), nullable = False)
    asterism = db.Column(db.String(30), nullable = True)
    description = db.Column(db.Text, nullable = True)
    #stars = db.relationship('Stars', backref = 'constellation', lazy = True)

    # Function to return a representation of a constellation entity when the database is queried
    def __repr__(self):
        return ''.join([
            'Constellation: ', self.name, '\r\n',
            'User: ', self.user, '\r\n',
            #'Num. of Associated Stars: ', self.num_stars, '\r\n',
            'Right Ascension: ', self.right_ascension, '\r\n',
            'Declination: ', self.declination, '\r\n',
            'Asterism: ', self.asterism, '\r\n',
            'Description: ', self.description
        ])
'''

class Observations(db.Model):
    # Table schema
    observationID = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String(100), nullable = False)
    userID = db.Column(db.Integer, db.ForeignKey('users.userID'), nullable = False) # foreign key
    #star = db.Column(db.Integer, ForeignKey('star.starID'), nullable = False) # foreign key
    #constellation = db.Column(db.Integer, ForeignKey('star.constellation'), nullable = False) # foreign key
    date_time = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    location = db.Column(db.String(100), nullable = False)
    azimuth = db.Column(db.Float, nullable = False)
    altitude = db.Column(db.Float, nullable = False)
    description = db.Column(db.Text, nullable = True)

    # Function to return a representation of an observations entity when the database is queried
    def __repr__(self):
        return ''.join([
            'User ID: ', self.userID, '\r\n',
            'Title: ', self.title, '\r\n',
            #'Star: ', self.star, '\r\n',
            #'Constellation: ', self.constellation, '\r\n',
            'Date and Time: ', self.date_time, '\r\n',
            'Location: ', self.location, '\r\n',
            'Azimuth: ', self.azimuth, '\r\n',
            'Altitude: ', self.altitude, '\r\n',
            'Description: ', self.description
        ])
'''
# Table to store star information
class Stars(db.Model):
    #__name__ = 'star'
    starID = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(50), nullable = False)
    constellation = db.Column(db.Integer, ForeignKey('constellation.constellationID')) # foreign key
    right_ascension = db.Column(db.String(30), nullable = False)
    declination = db.Column(db.String(30), nullable = False)
    #magnitude = db.Column(db.Integer, nullable = True)
    #num_observations = db.Column(db.Integer, nullable = False)
    description = db.Column(db.Text, nullable = True)
    observations = relationship('Observations', backref = 'star', lazy = True)

    # Function to return a representation of a star entity when the database is queried
    def __repr__(self):
        return ''.join([
            'Star: ', self.name, '\r\n',
            'Constellation: ', self.constellation, '\r\n',
            'Right Ascension: ', self.right_ascension, '\r\n',
            'Declination: ', self.declination, '\r\n',
            #'Magnitude: ', self.magnitude, '\r\n',
            #'Number of Observations: ', self.num_observations '\r\n',
            'Description: ', self.description
        ])
'''

