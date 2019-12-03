'''Main flask file to be run to start the app
Requires environment variables to be set in order to run
'''

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from os import getenv

app = Flask(__name__)
# Set login details from environment variables
user = getenv('MYSQL_USER')
password = getenv('MYSQL_PASSWORD')
db = getenv('MYSQL_DATABASE')
secret = getenv('MYSQL_SECRETKEY')

# Parse together the URI in order to connect to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + user + ':' + password + '@34.89.105.168/' + db
# Added security
app.config['SECRET_KEY'] = 'sd6g4d56s4g2s4dg54pu6456fdg45'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from flask_app import routes
