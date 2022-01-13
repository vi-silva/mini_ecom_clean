from src.domain.coupons.model import Coupons
from src.services.coupon.coupon_dto import CouponDTO
from src.services.sqlalchemy_uol import SqlAlchemyUnitOfWork

def create_coupon(couponDTO: CouponDTO, uow: SqlAlchemyUnitOfWork):
  with uow:
    coupon = uow.coupons_repository.get(code=couponDTO.code)
    if coupon:
      raise Exception()
    coupon = Coupons(**couponDTO.__dict__)
    coupon.verify_date()
    uow.coupons_repository.add(coupon)
    uow.commit()
