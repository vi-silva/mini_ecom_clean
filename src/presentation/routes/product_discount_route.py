from fastapi import APIRouter, status
from src.presentation.schemas.product_discounts_schema import CreateProductDiscountSchema
from src.services.product_discount.product_discounts_dto import ProductDiscountsDTO
from src.services.product_discount.product_discounts_service import create_product_discounts
from src.services.sqlalchemy_uol import SqlAlchemyUnitOfWork

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(schema: CreateProductDiscountSchema):
  uow = SqlAlchemyUnitOfWork()
  dto = ProductDiscountsDTO(**schema.dict())
  
  product_discount = create_product_discounts(dto, uow=uow)

  return product_discount