from sqlalchemy import create_engine
from .device import Device, Base
from sqlalchemy.orm import sessionmaker


class Storage:
    engine = None
    session = None

    def __init__(self) -> None:
        DB_USER = "admin"
        DB_PASSWORD = "S8SgÑ7m8QG#v"
        DB_HOST = "localhost"
        DB_NAME = "devices"
        self.engine = create_engine(
            f"mysql+mysqldb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
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
