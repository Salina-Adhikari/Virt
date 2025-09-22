import configparser
import config

config=configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getfirstname():
        firstname=config.get('common info','firstname')
        return firstname
    @staticmethod
    def getlastname():
        lastname=config.get('common info','lastname')
        return lastname

    @staticmethod
    def getemail():
        email=config.get('common info','email')
        return email
    @staticmethod
    def getpassword():
        password=config.get('common info','password')
        return password
    def getconfirmpass(self):
        password=config.get('common info','password')
        return password

    @staticmethod
    def getphonenumber():
        number=config.get('common info','phonenumber')
        return number
