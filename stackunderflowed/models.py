from pathlib import Path

from peewee import SqliteDatabase, CharField, DateField, Model

DATA_DIR: Path = Path.cwd() / "data"
db: SqliteDatabase = SqliteDatabase(DATA_DIR / "crypto.db")


class Participant(Model):
    pass

    class Meta:
        database = db


def connect_or_init_db() -> None:
    pass


def init_db():
    pass
