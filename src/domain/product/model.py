class Product:
  def __init__(self, description, price, technical_details, image, visible, supplier, category):
    self.description = description  
    self.price = price
    self.technical_details = technical_details
    self.image = image
    self.visible = visible
    self.supplier = supplier
    self.category = category

class Category:
  def __init__(self, name) -> None:
      self.name = name

class Suppliers:
  def __init__(self, name) -> None:
      self.name = name
    
class Coupons:
  def __init__(self, code, expire_at, limit, type, value) -> None:
      self.code = code
      self.expire_at = expire_at
      self.limit = limit
      self.type = type
      self.value = value

class PaymentMethods:
  def __init__(self, name, enabled) -> None:
      self.name = name
      self.enabled = enabled

class ProductDiscounts:
  def __init__(self, product, mode, value, payment_method) -> None:
      self.product = product
      self.mode = mode
      self.value = value
      self.payment_method = payment_method