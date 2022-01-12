from src.domain.category.model import Category
from src.services.sqlalchemy_uol import SqlAlchemyUnitOfWork

def create_category(name, uow: SqlAlchemyUnitOfWork):
  with uow:
    uow.category_repository.add(Category(name=name))
    uow.commit()
