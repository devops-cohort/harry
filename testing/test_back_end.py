import unittest

from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from flask_app import app, db
from flask_app.models import Users, Observations


class TestBase(TestCase):

    def create_app(self):

        # pass in test configurations
        config_name = 'testing'
        app.config.update(
            SQLALCHEMY_DATABASE_URI='mysql+pymysql://'+str(getenv('MYSQL_USER'))+':'+str(getenv('MYSQL_PASSWORD'))+'@'+str(getenv('MYSQL_URL'))+'/'+str(getenv('MYSQL_TEST_DB')))
        return app

    def setUp(self):
        """
        Will be called before every test
        """

        db.session.commit()
        db.drop_all()
        db.create_all()

        # create test admin user
        admin = Users(user_name = "admin", first_name="admin", last_name="admin", email="admin@admin.com", password="admin2016")

        # create test non-admin user
        employee = Users(user_name = "bob", first_name="test", last_name="user", email="test@user.com", password="test2016")

        # save users to database
        db.session.add(admin)
        db.session.add(employee)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class TestObservations(TestBase):

    def test_observation_model(self):
        '''
        Test the number of records in the observations table
        '''

        # Create an observation
        observation = Observations(title = 'test', userID = 1, location = 'test house', azimuth = 243.74, altitude = 36.24, description = 'this is a test post')

        db.session.add(observation)
        db.session.commit()

        self.assertEqual(Observations.query.count(), 1)
