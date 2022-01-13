from dataclasses import dataclass


@dataclass
class ProductDTO:
  description: str
  price: float
  technical_details: str
  image: str
  visible: bool
  categories_id: int
  suppliers_id: int