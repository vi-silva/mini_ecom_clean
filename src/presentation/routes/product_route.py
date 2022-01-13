from fastapi import APIRouter, status
from src.presentation.schemas.product_schema import CreateProductSchema
from src.services.product.product_dto import ProductDTO
from src.services.product.product_service import create_product
from src.services.sqlalchemy_uol import SqlAlchemyUnitOfWork

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(schema: CreateProductSchema):
  uow = SqlAlchemyUnitOfWork()
  dto = ProductDTO(**schema.dict())
  
  product = create_product(dto, uow=uow)

  return product