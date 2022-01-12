from src.domain.customers.model import Customers
from src.services.sqlalchemy_uol import SqlAlchemyUnitOfWork

def create_customer(first_name, last_name, phone_number, genre, document_id, birth_date, uow: SqlAlchemyUnitOfWork):
  with uow:
    uow.customers_repository.add(Customers(first_name=first_name, last_name=last_name, phone_number=phone_number, genre=genre, document_id=document_id, birth_date=birth_date))
    uow.commit()