'''Main flask run file'''
from flask_app import app
# Runs in debug mode and allows all connections
if __name__ == '__main__':
	app.run(debug = True, host = '0.0.0.0')
