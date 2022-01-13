from src.domain.payment_methods.model import PaymentMethods
from src.services.sqlalchemy_uol import SqlAlchemyUnitOfWork
from src.services.payment_method.payment_methods_dto import PaymentMethodsDTO

def create_payment_method(payment_methods_dto: PaymentMethodsDTO, uow: SqlAlchemyUnitOfWork):
  with uow:
    uow.payment_methods_repository.add(PaymentMethods(**payment_methods_dto.__dict__))
    uow.commit()