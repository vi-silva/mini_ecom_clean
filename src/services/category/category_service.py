from src.domain.category.model import Category
from src.services.sqlalchemy_uol import SqlAlchemyUnitOfWork
from src.services.category.category_dto import CategoryDTO

def create_category(categoryDTO: CategoryDTO, uow: SqlAlchemyUnitOfWork):
  with uow:
    uow.category_repository.add(Category(**categoryDTO.__dict__))
    uow.commit()
