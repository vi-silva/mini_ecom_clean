from pydantic import BaseModel

class CreateProductDiscountSchema(BaseModel):
    product_id : str
    mode : str
    value : float
    payment_methods_id : str