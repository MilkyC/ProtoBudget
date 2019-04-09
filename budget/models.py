from django.db import models


class Budget(models.Model):
  budget_id = models.AutoField(primary_key=True)


class BudgetPeriod(models.Model):
  budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
  name = models.CharField(max_length=100, unique=True)
  start_date = models.DateTimeField()
  end_date = models.DateTimeField()


class Category(models.Model):
  name = models.CharField(max_length=100, unique=True)


class Allotment(models.Model):
  budget_period = models.ForeignKey(BudgetPeriod, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  amount = models.DecimalField(max_digits=6, decimal_places=2)


class Expense(models.Model):
  budget_period = models.ForeignKey(BudgetPeriod, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  amount = models.DecimalField(max_digits=6, decimal_places=2)


class PeriodExpense(models.Model):
  budget_period = models.ForeignKey(BudgetPeriod, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  amount = models.DecimalField(max_digits=6, decimal_places=2)
  is_long_term = models.BooleanField()


class ExpenseSpent(models.Model):
  period_expense = models.ForeignKey(PeriodExpense, on_delete=models.CASCADE)
  date_spent = models.DateTimeField(auto_now_add=True)
  amount = models.DecimalField(max_digits=6, decimal_places=2)


class Income(models.Model):
  budget_period = models.ForeignKey(BudgetPeriod, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  amount = models.DecimalField(max_digits=6, decimal_places=2)
  date = models.DateTimeField(auto_now_add=True)
