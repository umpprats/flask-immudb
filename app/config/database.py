from flask import Flask
from immudb import ImmudbClient
from immudb.datatypesv2 import DatabaseSettingsV2

class ImmuDataBase():
    def __init__(self) -> None:
        self.__immu_db = None

    def init_app(self, app: Flask) -> None:
        db = app.config['IMMUDB_DB']
        user = app.config['IMMUDB_USER']
        password = app.config['IMMUDB_PASSWORD']
        host = app.config['IMMUDB_HOST']
        port = app.config['IMMUDB_PORT']
        print(f'Connecting to immudb {host}:{port} with database {db} and user {user}')
        self.__immu_db = ImmudbClient(f'{host}:{port}')
        self.__immu_db.login(user, password)
        self.__immu_db.createDatabaseV2(db, settings=DatabaseSettingsV2(),ifNotExists=True)
        self.__immu_db.useDatabase(db.encode('utf8'))
    
    def client(self):
        return self.__immu_db