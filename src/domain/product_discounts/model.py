from src.domain.payment_methods.model import PaymentMethods

class ProductDiscounts:
  def __init__(self, product , mode, value, payment_method: PaymentMethods) -> None:
      self.product = product
      self.products_id = product.id
      self.mode = mode
      self.value = value
      self.payment_method = payment_method
      self.payment_methods_id = payment_method.id