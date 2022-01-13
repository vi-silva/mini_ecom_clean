from datetime import datetime


class Coupons:
  def __init__(self, code, expire_at, limit, type, value) -> None:
      self.code = code
      self.expire_at = expire_at
      self.limit = limit
      self.type = type
      self.value = value

  def verify_date(self):
    if datetime.now() > self.expire_at:
      raise Exception()