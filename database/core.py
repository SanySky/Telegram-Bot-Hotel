from database.utils.CRUD import CRUDInterface
from database.common.models import db, Histori

db.connect()
db.create_tables([Histori])

crud = CRUDInterface()

if __name__ == '__main__':
    crud()
