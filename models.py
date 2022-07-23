import string

from sqlalchemy import Column, Integer, String, Float

import db


class Operation(db.Base):
    __tablename__ = "operation"
    id = Column(Integer, primary_key=True)
    date = Column(String(8))
    type_operation = Column(String(7))
    description = Column(String(50))
    amount = Column(Float)

    def __init__(self, date: string, type_operation: string, description: string, amount: float):
        super(Operation, self).__init__()
        self.date = date
        self.type_operation = type_operation
        self.description = description
        self.amount = amount

    def __str__(self):
        return f'Operation: {self.id}, {self.date}, {self.type_operation}, {self.description}, {self.amount}'
