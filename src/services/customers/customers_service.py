from src.domain.addresses.model import Addresses
from src.domain.customers.model import Customers
from src.services.customers.customer_dto import CustomerDTO
from src.services.sqlalchemy_uol import SqlAlchemyUnitOfWork
from src.services.address.address_dto import AddressDTO

def create_customer(customerDTO: CustomerDTO, uow: SqlAlchemyUnitOfWork):
  with uow:
    uow.customers_repository.add(Customers(**customerDTO.__dict__))
    uow.commit()

def create_address(addressDTO: AddressDTO, uow: SqlAlchemyUnitOfWork):
  with uow:
    customer = uow.customers_repository.get(id=addressDTO.customer_id)
    if not customer:
      return Exception
    address =  Addresses(address=addressDTO.address,
                         city=addressDTO.city,
                         state=addressDTO.state,
                         number=addressDTO.number,
                         zipcode=addressDTO.zipcode,
                         neighbourhood=addressDTO.neighbourhood,
                         primary=addressDTO.primary,
                         customer_id=addressDTO.customer_id,
                         customer=customer)
    customer.add_address(address)
    uow.commit()