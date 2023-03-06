class Config(object):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///agendas.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False