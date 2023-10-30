from datetime import datetime

import peewee as pw

db = pw.SqliteDatabase('lecture.db')

class ModelBase(pw.ModelBase):
    created_at = pw.DateField(default=datetime.now())

    class Meta():
        datebase = db

class Histori(ModelBase):
    number = pw.TextField()
    massage = pw.TextField()