class Config:
    SECRET_KEY = b"\x92\xdf\x91\x058\x8e\x1e\xfe\x95v\xc4'\xb5\r\x1f\xd8\x08\x8c\xc5 \x8d%\xbeM"
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://test:test@db/test"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Development(Config):
    Debug=True

class Testing(Config):
    pass

config = {
    "development": Development
}


# """Flask config class."""
# import os


# class Config:
#     """Set Flask configuration vars."""

#     # General Config
#     TESTING = True
#     DEBUG = True
#     SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
#     SESSION_COOKIE_NAME = 'my_cookie'

#     # Database
#     SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI',
#                                              'postgresql+psycopg2://test:test@0.0.0.0:5401/test')
#     SQLALCHEMY_USERNAME = 'test'
#     SQLALCHEMY_PASSWORD = 'test'
#     SQLALCHEMY_DATABASE_NAME = 'test'
#     SQLALCHEMY_TABLE = 'migrations'
#     SQLALCHEMY_DB_SCHEMA = 'public'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
