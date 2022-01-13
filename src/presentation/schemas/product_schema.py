from pydantic import BaseModel

class CreateProductSchema(BaseModel):
  description: str
  price: float
  technical_details: str
  image: str
  visible: bool
  categories_id: int
  suppliers_id: int