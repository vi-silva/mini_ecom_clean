class ValidationUtils:
    def __init__(self, repository) -> None:
        self.repository = repository
        

    def validate_discount(self, products_id, payment_methods_id):
        if self.repository.get_by_product_and_payment(products_id,payment_methods_id):
            raise Exception()
