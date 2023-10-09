from app.models import Auditable
from app import db

class AuditableRepository:
    def __init__(self):
        self.__db = db
    
    def create(self, entity: Auditable)-> int:
        insert_sql = f"INSERT INTO auditable (created_at, created_by, filename, hash) VALUES ('{entity.created_at}', '{entity.created_by}', '{entity.filename}', '{entity.hash}');"
        
        response = self.__db.client().sqlExec(insert_sql)
        return response.txs[0].lastInsertedPKs['auditable'].n
    
    def upsert(self, entity: Auditable):
        update_sql = f"UPSERT INTO auditable (created_at, created_by, filename, hash) VALUES ('{entity.created_at}', '{entity.created_by}', '{entity.filename}', '{entity.hash}');"
        print(update_sql)
        response = self.__db.client().sqlExec(update_sql)
        print(response.txs[0].updatedRows['auditable'].n)
