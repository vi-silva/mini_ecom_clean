from pydantic import BaseModel

class CreateProductDiscountSchema(BaseModel):
    product_id : int
    mode : str
    value : float
    payment_methods_id : int