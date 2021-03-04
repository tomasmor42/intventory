import os

class Config:
 
    DEBUG = os.environ.get("DEBUG", False)
    HOST = os.environ.get("HOST", "127.0.0.1")
    PORT = os.environ.get("PORT", "5000")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", "sqlite:///warehouse.db")
    TEST_DATABASE = os.environ.get("TEST_DATABASE", "tmpfile.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS", True)