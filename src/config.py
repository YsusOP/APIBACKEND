class DevelopmentConfig:
    DEBUG = True
    MYSQL_HOST = 'basededatos.mysql.database.azure.com'
    MYSQL_USER = 'exercise'
    MYSQL_PASSWORD = '57951227Pumba'
    MYSQL_DB = 'mydb'

class ProductionConfig:
    DEBUG = False
    MYSQL_HOST = 'basededatos.mysql.database.azure.com'
    MYSQL_USER = 'exercise'
    MYSQL_PASSWORD = '57951227Pumba'
    MYSQL_DB = 'mydb'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}