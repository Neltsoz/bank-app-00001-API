from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey
)
from sqlalchemy.orm import relationship

from app.database import Base


class Payment(Base):
    __tablename__ = 'payments'

    transaction_id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Float)
    signature = Column(String)

    user = relationship('User', backref='payments')
    account = relationship('Account', backref='payments')
