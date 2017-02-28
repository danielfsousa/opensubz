import configparser
import os
import sys


class Config:

    PATH = os.path.join(sys.prefix, 'config', 'opensubz.ini')
    OPENSUBTITLES = 'opensubtitles'
    EMAIL = 'email'
    PASSWORD = 'password'
    LANGUAGE = 'language'

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(Config.PATH)

        self.email = self.config.get(Config.OPENSUBTITLES, Config.EMAIL)
        self.password = self.config.get(Config.OPENSUBTITLES, Config.PASSWORD)
        self.language = self.config.get(Config.OPENSUBTITLES, Config.LANGUAGE)

    def save(self):
        self.config.set(Config.OPENSUBTITLES, Config.EMAIL, self.email)
        self.config.set(Config.OPENSUBTITLES, Config.PASSWORD, self.password)
        self.config.set(Config.OPENSUBTITLES, Config.LANGUAGE, self.language)
        with open(Config.PATH, 'w') as configfile:
            self.config.write(configfile)
