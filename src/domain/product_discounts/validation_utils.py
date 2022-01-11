class ValidationUtils:
    def __init__(self, repository) -> None:
        self.repository = repository
        

    def validate_discount(self, product_discount):
        if self.repository.get_by_product_and_payment(product_discount.products_id,product_discount.payment_methods_id) or product_discount.payment_method.enabled == False:
            raise Exception()
        
