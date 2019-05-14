from django.urls import include, path
from rest_framework import routers

from . import api 
from . import views

router = routers.DefaultRouter()
router.register('budgetperiod', api.BudgetPeriodViewSet)
router.register('categories', api.CategoryViewSet)
router.register('allotments', api.AllotmentViewSet)
router.register('periodexpense', api.PeriodExpenseViewSet)
router.register('expense', api.ExpenseViewSet)
router.register('expensespent', api.ExpenseSpentViewSet)
router.register('income', api.IncomeViewSet)

urlpatterns = [
    path('', views.index),
    path('api/', include(router.urls)),
    path('<int:budget_period_id>', views.index),
]
