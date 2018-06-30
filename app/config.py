import os


class Config(object):
    """
    Base config class.
    """
    DEBUG = False
    TESTING = False

    SECRET_KEY = '97cce08ed5f5ff4c4689dd789d22147d531199cbcbeb6e272481bf3921fa13d653496b966fe232f0038208db58cc4710'
    LOGFILE_PATH = os.environ.get('LOGFILE_PATH', 'log/app.log')


class LocalConfig(Config):
    """
    local config.
    """
    DEBUG = True


class DevelopmentConfig(Config):
    """
    dev environment config.
    """
    DEBUG = True


class TestingConfig(Config):
    """
    testing config.
    """
    TESTING = True


class ProductionConfig(Config):
    """
    production config.
    """
    pass
