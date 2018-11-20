import json
from flask_testing import TestCase
from run import app
from app.database import Database

from app.api.v2.models.user import User
from app.api.v2.models.parcel import Parcel


class BaseTestCase(TestCase):
    """ Base Tests """

    @classmethod
    def create_app(cls):
        app.config.from_object('instance.config.TestingConfig')
        return app

    def setUp(self):
        self.db = Database(testing="testing")
        self.cursor = self.db.cursor
        self.dict_cursor = self.db.dict_cursor
        self.db.create_tables()
        
        self.user = User(
            user_id=1,
            username="kamardaniel",
            email='kamardaniel@gmail.com',
            password='password',
            confirm='password'
        )
        self.parcel_obj = Parcel(
            parcel_id=1,
            parcel_name="first parcel model test",
            status='testing is very essential',
            price=1,
            pickup_location="Nairobi",
            destination_location="Mombasa",
            user_id="1"
        )
        self.parcel = json.dumps(
            {
                "parcel_name": "first test",
                "pickup_location": "DROP VAN",
                "destination_location": "MOMBASA",
                "price": 1000,
                "status": "tdd is awesome"
            }
        )
        self.parcel_no_parcel_name = json.dumps(
            {
                "parcel_name": "",
                "pickup_location": "DROP VAN",
                "destination_location": "MOMBASA",
                "price": 1000,
                "status": "tdd is awesome"
            }
        )
        self.parcel_no_status = json.dumps(
            {
                "parcel_name": "first test",
                "pickup_location": "DROP VAN",
                "destination_location": "MOMBASA",
                "price": 1000,
                "status": ""
            }
        )
        self.update_parcel = json.dumps(
            {
                "parcel_name": "first edition",
                "pickup_location": "DROP VAN",
                "destination_location": "MOMBASA",
                "price": 1000,
                "status": "tdd is very awesome"
            }
        )

    def tearDown(self):
        self.db.drop_all()