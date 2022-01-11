from src.domain.payment_methods.model import PaymentMethods
from src.adapter.sqlalchemy_repository import SqlAlchemyRepository


class PaymentMethodsRepository(SqlAlchemyRepository[PaymentMethods]):
  pass