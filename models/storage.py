from sqlalchemy import create_engine
from .device import Device, Base
from sqlalchemy.orm import sessionmaker
from os import getenv
from dotenv import load_dotenv


load_dotenv()


class Storage:
    engine = None
    session = None

    def __init__(self) -> None:
        DB_USER = getenv('DB_USER')
        DB_PASSWORD = getenv('DB_PASSWORD')
        DB_HOST = getenv('DB_HOST')
        DB_NAME = getenv('DB_NAME')
        self.engine = create_engine(
            f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
        )

    def all(self):
        return self.session.query(Device).all()
    
    def delete(self, item):
        if item is not None:
            self.session.delete(item)
    
    def get(self, id):
        return self.session.get(Device, id)

    def load_session(self):
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def new(self, item):
        self.session.add(item)

    def save(self):
        self.session.commit()
