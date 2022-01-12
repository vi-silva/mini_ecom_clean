from src.domain.addresses.model import Addresses
from src.services.sqlalchemy_uol import SqlAlchemyUnitOfWork

def create_address(address, city, state, number, zipcode, neighbourhood, primary, customer_id, uow: SqlAlchemyUnitOfWork):
  with uow:
    uow.addresses_repository.add(Addresses(address=address, city=city, state=state, number=number, zipcode=zipcode, neighbourhood=neighbourhood, primary=primary, customer_id=customer_id))
    uow.commit()