from .db_connect import Base


from sqlalchemy import Column, Integer


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
