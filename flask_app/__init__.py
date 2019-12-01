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
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + user + ':' + password + '@34.89.105.168/' + db
db = SQLAlchemy(app)
# Added security
app.config['SECRET_KEY'] = '65s4df21rt354sd32rf4g354s3d5f424r4ts3dajk4l35'

from flask_app import routes
