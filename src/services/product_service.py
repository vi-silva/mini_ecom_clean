from src.domain.product.model import Product
from src.services.sqlalchemy_uol import SqlAlchemyUnitOfWork

def create_product( description  , price, technical_details, image, visible, suppliers_id, categories_id, uow: SqlAlchemyUnitOfWork):
  with uow:
    uow.product_repository.add(Product( description = description, price = price, technical_details = technical_details, image = image, visible = visible, suppliers_id = suppliers_id, categories_id = categories_id))
    uow.commit()