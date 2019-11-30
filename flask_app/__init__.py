'''Main flask file to be run to start the app
Requires environment variables to be set in order to run
'''

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
# Set login details from environment variables
user = getenv('MYSQL_USER')
password = getenv('MYSQL_PASSWORD')
db = getenv('MYSQL_DATABASE')

# Parse together the URI in order to connect to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + user + ':' + password + '@35.197.245.254/' + db
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = '7218a9143c27c16610765205a1b21cb7'

from application import routes