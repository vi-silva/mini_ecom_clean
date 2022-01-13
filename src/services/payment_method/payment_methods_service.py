from src.domain.payment_methods.model import PaymentMethods
from src.services.sqlalchemy_uol import SqlAlchemyUnitOfWork

def create_payment_method(name, enabled, uow: SqlAlchemyUnitOfWork):
  with uow:
    uow.payment_methods_repository.add(PaymentMethods(name = name, enabled = enabled))
    uow.commit()