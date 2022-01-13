from src.domain.suppliers.model import Suppliers
from src.services.sqlalchemy_uol import SqlAlchemyUnitOfWork
from src.services.suppliers.suppliers_dto import SuppliersDTO

def create_supplier(supplier_dto: SuppliersDTO, uow: SqlAlchemyUnitOfWork):
    with uow:
        uow.supplier_repository.add(Suppliers(**supplier_dto.__dict__))
        uow.commit()
