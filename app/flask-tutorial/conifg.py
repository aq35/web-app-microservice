class SystemConfig:

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
        'user': 'root',
        'password': 'password',
        'host': 'mysql',
        'db_name': 'flask-app'
    })


# 外部ファイルから読み込める様にしている。
Config = SystemConfig
