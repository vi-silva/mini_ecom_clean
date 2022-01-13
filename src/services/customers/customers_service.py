from src.domain.addresses.model import Addresses
from src.domain.customers.model import Customers
from src.services.customers.customer_dto import CustomerDTO
from src.services.sqlalchemy_uol import SqlAlchemyUnitOfWork

def create_customer(customerDTO: CustomerDTO, uow: SqlAlchemyUnitOfWork):
  with uow:
    uow.customers_repository.add(Customers(**customerDTO.__dict__))
    uow.commit()

def create_address(address, city, state, number, zipcode, neighbourhood, primary, customer_id, uow: SqlAlchemyUnitOfWork):
  with uow:
    customer = uow.customers_repository.get(id=customer_id)
    if not customer:
      return Exception
    address =  Addresses(address=address, city=city, state=state, number=number, zipcode=zipcode, neighbourhood=neighbourhood, primary=primary, customer_id=customer_id, customer=customer)
    customer.add_address(address)
    uow.commit()