
import os
import tempfile

import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from config import Config   
from app import app, ma, create_app
from app.models import db

@pytest.fixture
def products_json():
    return {
  "products": [
    {
      "name": "Dining Chair",
      "contain_articles": [
        {
          "art_id": "1",
          "amount_of": "4"
        },
        {
          "art_id": "2",
          "amount_of": "8"
        },
        {
          "art_id": "3",
          "amount_of": "1"
        }
      ]
    },
    {
      "name": "Dinning Table",
      "contain_articles": [
        {
          "art_id": "1",
          "amount_of": "4"
        },
        {
          "art_id": "2",
          "amount_of": "8"
        },
        {
          "art_id": "4",
          "amount_of": "1"
        }
      ]
    }
  ]
}
@pytest.fixture
def inventory_json():
    return {
  "inventory": [
    {
      "art_id": "1",
      "name": "leg",
      "stock": "12"
    },
    {
      "art_id": "2",
      "name": "screw",
      "stock": "17"
    },
    {
      "art_id": "3",
      "name": "seat",
      "stock": "2"
    },
    {
      "art_id": "4",
      "name": "table top",
      "stock": "1"
    }
  ]
}


@pytest.fixture
def app_fixture():
    app.config['TESTING'] = True
    app.config['DEBUG'] = False
    test_db, app.config['TEST_DATABASE'] = tempfile.mkstemp()
    with app.app_context():
        db.init_app(app)
        ma.init_app(app)
        db.create_all()
    yield app

    os.close(test_db)
    os.unlink(app.config['TEST_DATABASE'])

@fixture
def client(app_fixture):
    return app_fixture.test_client()

@pytest.fixture
def base_url(app_fixture):
    return 'http://' + app_fixture.config.get('HOST') + ":" + app_fixture.config.get('PORT')