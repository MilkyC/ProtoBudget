from budget.models import Allotment, Budget, BudgetPeriod, Category, Expense, ExpenseSpent, Income, PeriodExpenseAllotment, PeriodExpense
from rest_framework import serializers


class BudgetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Budget
        fields = ('budget_id')


class BudgetPeriodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BudgetPeriod 
        fields = ('id', 'name')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category 
        fields = ('id', 'name', 'default_allotment')


class AllotmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Allotment 
        fields = ('id', 'budget_period', 'category', 'amount')


class PeriodExpenseAllotmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PeriodExpenseAllotment
        fields = ('id', 'default_allotment', 'is_long_term')


class PeriodExpenseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PeriodExpense 
        fields = ('id', 'budget_period', 'amount', 'period_expense_allotment')


class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Expense 
        fields = ('id', 'budget_period', 'category', 'name', 'amount')


class ExpenseSpentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExpenseSpent 
        fields = ('id', 'period_expense', 'date_spent', 'amount')


class IncomeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Income 
        fields = ('id', 'budget_period', 'name', 'date', 'amount')

