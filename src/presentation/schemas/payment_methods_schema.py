from pydantic import BaseModel

class CreatePaymentMethodsSchema(BaseModel):
    name : str
    enabled : bool