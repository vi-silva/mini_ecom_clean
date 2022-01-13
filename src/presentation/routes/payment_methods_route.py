from fastapi import APIRouter, status
from src.presentation.schemas.payment_methods_schema import CreatePaymentMethodsSchema
from src.services.payment_method.payment_methods_dto import PaymentMethodsDTO
from src.services.payment_method.payment_methods_service import create_payment_method
from src.services.sqlalchemy_uol import SqlAlchemyUnitOfWork

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(schema: CreatePaymentMethodsSchema):
  uow = SqlAlchemyUnitOfWork()
  dto = PaymentMethodsDTO(**schema.dict())
  
  payment_methods = create_payment_method(dto, uow=uow)

  return payment_methods