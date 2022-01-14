from fastapi import APIRouter, status
from src.presentation.schemas.customer_schema import CreateCustomerSchema
from src.services.customers.customer_dto import CustomerDTO
from src.services.customers.customers_service import create_customer
from src.services.sqlalchemy_uol import SqlAlchemyUnitOfWork

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(schema: CreateCustomerSchema):
  uow = SqlAlchemyUnitOfWork()
  dto = CustomerDTO(**schema.dict())
  
  customer = create_customer(dto, uow=uow)

  return customer