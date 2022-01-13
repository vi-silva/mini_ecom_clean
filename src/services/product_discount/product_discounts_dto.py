from dataclasses import dataclass
from src.domain.payment_methods.model import PaymentMethods

from src.domain.product.model import Product

@dataclass
class ProductDiscountsDTO:
    product_id : int
    mode : str
    value : float
    payment_methods_id : int
    product: Product = None
    payment_method: PaymentMethods = None