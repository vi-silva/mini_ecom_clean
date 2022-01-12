from src.domain.suppliers.model import Suppliers
from src.services.sqlalchemy_uol import SqlAlchemyUnitOfWork


def create_supplier(name, uow: SqlAlchemyUnitOfWork):
    with uow:
        uow.supplier_repository.add(Suppliers(name=name))
