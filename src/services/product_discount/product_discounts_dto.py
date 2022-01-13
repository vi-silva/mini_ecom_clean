from dataclasses import dataclass

@dataclass
class ProductDiscountsDTO:
    product_id : str
    mode : str
    value : float
    payment_methods_id : str