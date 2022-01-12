from src.domain.coupons.model import Coupons
from src.services.sqlalchemy_uol import SqlAlchemyUnitOfWork

def create_coupon(code, expire_at, limit, type, value, uow: SqlAlchemyUnitOfWork):
  with uow:
    uow.coupons_repository.add(Coupons(code=code, expire_at=expire_at, limit=limit, type=type, value=value))
    uow.commit()
