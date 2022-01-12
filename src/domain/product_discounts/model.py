from src.domain.payment_methods.model import PaymentMethods

class ProductDiscounts:
  def __init__(self, product_id , mode, value, payment_methods_id: PaymentMethods) -> None:
      self.products_id = product_id
      self.mode = mode
      self.value = value
      self.payment_methods_id = payment_methods_id