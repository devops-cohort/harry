import unittest

from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from flask_app import app, db
from flask_app.models import Users, Observations, observers


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
        admin = Users(user_name = "admin", first_name="admin", last_name="admin", email="admin@admin.com", password="test")

        # create test non-admin users
        user1 = Users(user_name = "test1", first_name="test", last_name="user", email="test1@user.com", password="test")
        user2 = Users(user_name = "test2", first_name="test", last_name="user", email="test2@user.com", password="test")

        # save users to database
        db.session.add(admin)
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class TestObservations(TestBase):

    def test_observation_post_access_denied(self):
        '''
        Test that the user cannot access the 'enter observations' page without being logged in
        and is therefore redirected
        '''

        response = self.client.get(url_for('enterobservation'))
        self.assertEqual(response.status_code, 302)

    def test_observation_model(self):
        '''
        Test the number of records in the observations table
        '''

        # Create an observation
        observation = Observations(
            title = 'test', 
            author = 'admin', 
            location = 'test house', 
            azimuth = 243.74, 
            altitude = 36.24, 
            description = 'this is a test post'
        )
        # Add observation to database and commit
        db.session.add(observation)
        db.session.commit()
        # Assert that there should be 1 observation in the table
        self.assertEqual(Observations.query.count(), 1)

    def test_association_table(self):
        '''
        Test that multiple users can be associated with an observation
        '''

        # Find and save observation in table to variable 'observation'
        observation = Observations.query.filter_by(title = 'test').all()
        # Find and save two test users to variables 'user1' and 'user2'
        user1 = Users.query.filter_by(user_name = 'test1').first()
        user2 = Users.query.filter_by(user_name = 'test2').first()
        # Create the association
        observation.observers.append(user1)
        observation.observers.append(user2)
        # Commit to the database
        db.session.commit()
        # Create joining table of observers' usernames and observations' obersation IDs
        # Should be saved as a list of tuples
        observers_for_observation = db.session.query(Users.user_name, Observations.observationID).outerjoin(Observations, Users.userID == Observations.observer.userID).all()
        # Asser that user1 and user2 should be associated with observation with observationID 1
        self.assertEqual(observers_for_observation[0], ('test1', 1))
        self.assertEqual(observers_for_observation[1], ('test2', 1))

class TestLogin(TestBase):

    def test_login_view(self):
        '''
        Test that login is accessible without being logged in
        '''
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)

class TestSignUp(TestBase):

    def test_sign_up_view(self):
        '''
        Test that sign up page is accessible without being logged in
        '''
        response = self.client.get(url_for('signup'))
        self.assertEqual(response.status_code, 200)

