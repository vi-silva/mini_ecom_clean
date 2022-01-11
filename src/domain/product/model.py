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