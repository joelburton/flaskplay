"""Configuration classes for different modes of application."""


class Config(object):
    """Common configuration choices."""

    SHELVE_FILENAME = "store.shelve"


class DevConfig(Config):
    """Development configuration mode."""

    DEBUG = True


class TestConfig(Config):
    """Testing configuration mode."""

    TESTING = True
