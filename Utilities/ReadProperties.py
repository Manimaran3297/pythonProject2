import configparser
config = configparser.RawConfigParser()
config.read("/Users/ticvictech/PycharmProjects/pythonProject2/Configurations/config.ini")
class ReadConfig():
    @staticmethod
    def getApplicationURL():
         url=config.get("common info","baseURl")
         return url

    @staticmethod
    def getPassword():
        password = config.get("common info","password")
        return password

    @staticmethod
    def getUsername():
        username = config.get("common info", "username")
        return username

