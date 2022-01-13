from src.domain.product.model import Product
from src.services.sqlalchemy_uol import SqlAlchemyUnitOfWork
from src.services.product.product_dto import ProductDTO

def create_product( productDTO: ProductDTO, uow: SqlAlchemyUnitOfWork):
  with uow:
    uow.product_repository.add(Product(**productDTO.__dict__))
    uow.commit()