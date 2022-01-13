from src.domain.coupons.model import Coupons
from src.services.sqlalchemy_uol import SqlAlchemyUnitOfWork
from datetime import datetime

def create_coupon(code, expire_at, limit, type, value, uow: SqlAlchemyUnitOfWork):
  with uow:
    coupon = uow.coupons_repository.get(code=code)
    if coupon:
      raise Exception()
    coupon = Coupons(code=code, expire_at=expire_at, limit=limit, type=type, value=value)
    coupon.verify_date()
    uow.coupons_repository.add(coupon)
    uow.commit()
