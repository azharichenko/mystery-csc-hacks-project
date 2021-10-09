from peewee import SqliteDatabase, CharField, DateField, Model

from stackunderflowed import DATA_DIR

db: SqliteDatabase = SqliteDatabase(DATA_DIR / "crypto.db")


class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db  # This model uses the "people.db" database.


def init_db():
    pass
