from fastapi import APIRouter, status
from src.presentation.schemas.suppliers_schema import CreateSupplierSchema
from src.services.suppliers.suppliers_dto import SuppliersDTO
from src.services.suppliers.suppliers_service import create_supplier
from src.services.sqlalchemy_uol import SqlAlchemyUnitOfWork

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(schema: CreateSupplierSchema):
  uow = SqlAlchemyUnitOfWork()
  dto = SuppliersDTO(**schema.dict())
  
  suppliers = create_supplier(dto, uow=uow)

  return suppliers