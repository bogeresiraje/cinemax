import os


class Configuration(object):
    DEBUG = True
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:12345@cinemaxapp.herokuapp.com/:5432/cinemax_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
