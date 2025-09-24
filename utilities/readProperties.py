import configparser
import os
config = configparser.RawConfigParser()

config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "configurations", "config.ini")
config.read(config_path)

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('base info','baseurl')
        return url

    @staticmethod
    def getfirstname():
        firstname=config.get('base info','firstname')
        return firstname
    @staticmethod
    def getlastname():
        lastname=config.get('base info','lastname')
        return lastname

    @staticmethod
    def getemail():
        email=config.get('base info','email')
        return email
    @staticmethod
    def getpassword():
        password=config.get('base info','password')
        return password

    @staticmethod
    def getphonenumber():
        number=config.get('base info','phonenumber')
        return number
    @staticmethod
    def getvalidcode():
        code=config.get('base info','validcode')
        return code

