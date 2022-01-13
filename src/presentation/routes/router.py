from fastapi import APIRouter
from src.presentation.routes.product_route import router as product_router
from src.presentation.routes.category_route import router as category_router
from src.presentation.routes.coupon_route import router as coupon_router
from src.presentation.routes.payment_methods_route import router as payment_methods_router
from src.presentation.routes.product_discount_route import router as product_discount_router
from src.presentation.routes.suppliers_route import router as suppliers_router

router = APIRouter()

router.include_router(product_router, prefix='/products', tags=['product'])
router.include_router(category_router, prefix="/category", tags=['category'])
router.include_router(coupon_router, prefix="/coupon", tags=['coupon'])
router.include_router(payment_methods_router, prefix="/payment_methods", tags=['payment_methods'])
router.include_router(product_discount_router, prefix="/product_discount", tags=['product_discount'])
router.include_router(suppliers_router, prefix="/suppliers", tags=['suppliers'])

