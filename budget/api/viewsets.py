from budget.models import Category
from rest_framework import viewsets
from .serializers import * 


class BudgetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows budget to be viewed or edited.
    """

    serializer_class = BudgetSerializer
    queryset = Budget.objects.all()


class BudgetPeriodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows BudgetPeriod to be viewed or edited.
    """

    serializer_class = BudgetPeriodSerializer
    queryset = BudgetPeriod.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """

    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class AllotmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Allotment to be viewed or edited.
    """

    serializer_class = AllotmentSerializer
    queryset = Allotment.objects.all()


class PeriodExpenseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows PeriodExpense to be viewed or edited.
    """

    serializer_class = PeriodExpenseSerializer
    queryset = PeriodExpense.objects.all()


class PeriodExpenseAllotmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows PeriodExpense to be viewed or edited.
    """

    serializer_class = PeriodExpenseAllotmentSerializer
    queryset = PeriodExpenseAllotment.objects.all()


class ExpenseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Expense to be viewed or edited.
    """

    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()


class ExpenseSpentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ExpenseSpent to be viewed or edited.
    """

    serializer_class = ExpenseSpentSerializer
    queryset = ExpenseSpent.objects.all()


class IncomeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Income to be viewed or edited.
    """

    serializer_class = IncomeSerializer
    queryset = Income.objects.all()
