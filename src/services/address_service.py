from src.domain.addresses.model import Addresses
from src.services.sqlalchemy_uol import SqlAlchemyUnitOfWork

def create_address(address, city, state, number, zipcode, neighbourhood, primary, customer_id, uow: SqlAlchemyUnitOfWork):
  with uow:
    customer = uow.customers_repository.get(id=customer_id)
    if not customer:
      return Exception
    address =  Addresses(address=address, city=city, state=state, number=number, zipcode=zipcode, neighbourhood=neighbourhood, primary=primary, customer_id=customer_id, customer=customer)
    customer.add_address(address)
    for address in customer.addresses:
      uow.addresses_repository.add(address)
    uow.commit()