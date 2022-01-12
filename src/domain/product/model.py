from typing import List
from src.domain.product_discounts.model import ProductDiscounts


class Product:
  def __init__(self, description, price, technical_details, image, visible, supplier, category):
    self.description = description  
    self.price = price
    self.technical_details = technical_details
    self.image = image
    self.visible = visible
    self.supplier = supplier
    self.suppliers_id = supplier.id
    self.category = category
    self.categories_id = category.id
    self.discounts : List[ProductDiscounts] = []

    def add_discount(self, discount: ProductDiscounts):
        if not discount.payment_method.enabled:
            raise Exception('Este método de pagamento não está disponível')
        
        has_discount = len(list(filter(lambda d: d.payment_method.id == discount.payment_method.id, self.discounts))) > 0
        if has_discount:
            raise Exception(f'Já existe um desconto para este método de pagammento: {discount.payment_method.name}')

        
        self.discounts.append(discount)