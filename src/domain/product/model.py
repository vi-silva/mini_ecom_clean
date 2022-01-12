from typing import List
from src.domain.category.model import Category
from src.domain.product_discounts.model import ProductDiscounts
from src.domain.suppliers.model import Suppliers


class Product:
  def __init__(self, description, price, technical_details, image, visible, suppliers_id, categories_id):
    self.description = description  
    self.price = price
    self.technical_details = technical_details
    self.image = image
    self.visible = visible
    self.supplier: Suppliers
    self.suppliers_id = suppliers_id
    self.category: Category
    self.categories_id = categories_id
    self.discounts : List[ProductDiscounts] = []

    def add_discount(self, discount: ProductDiscounts):
        if not discount.payment_method.enabled:
            raise Exception('Este método de pagamento não está disponível')
        
        has_discount = len(list(filter(lambda d: d.payment_method.id == discount.payment_method.id, self.discounts))) > 0
        if has_discount:
            raise Exception(f'Já existe um desconto para este método de pagammento: {discount.payment_method.name}')

        
        self.discounts.append(discount)