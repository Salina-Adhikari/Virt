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
    def getpassword():
        password=config.get('base info','password')
        return password

    @staticmethod
    def getphonenumber():
        number=config.get('base info','phonenumber')
        return number

    @staticmethod
    def getname():
        name=config.get('agency info','name')
        return name
    @staticmethod
    def getrole():
        role=config.get('agency info','role')
        return role

    @staticmethod
    def getagency_email():
        email=config.get('agency info','agency_email')
        return email
    @staticmethod
    def getwebsite():
        website=config.get('agency info','website')
        return website

    @staticmethod
    def getaddress():
        address = config.get('agency info', 'address')
        return address
    @staticmethod
    def getcountry():
        country=config.get('agency info','country')
        return country


