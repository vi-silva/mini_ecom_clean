from src.domain.customers.model import Customers
from src.adapter.sqlalchemy_repository import SqlAlchemyRepository


class CustomersRepository(SqlAlchemyRepository[Customers]):
  pass