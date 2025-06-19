from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseViewSet, budget_status

router = DefaultRouter()
router.register(r"expenses", ExpenseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('status/', budget_status),
]
