from dataclasses import dataclass

@dataclass
class PaymentMethodsDTO:
    name : str
    enabled : bool