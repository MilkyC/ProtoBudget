from django.db import models


class Budget(models.Model):
  budget_id = models.AutoField(primary_key=True)


class BudgetPeriod(models.Model):
  budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
  name = models.CharField(max_length=100, unique=True)
  start_date = models.DateTimeField()
  end_date = models.DateTimeField()

  def __str__(self):
    return '{}'.format(self.name)


class Category(models.Model):
  name = models.CharField(max_length=100, unique=True)
  default_allotment = models.DecimalField(max_digits=6, decimal_places=2)

  def __str__(self):
    return '{}'.format(self.name)


class Allotment(models.Model):
  budget_period = models.ForeignKey(BudgetPeriod, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  amount = models.DecimalField(max_digits=6, decimal_places=2)

  def __str__(self):
    return '{} {}'.format(self.category, self.amount)


class Expense(models.Model):
  budget_period = models.ForeignKey(BudgetPeriod, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  amount = models.DecimalField(max_digits=6, decimal_places=2)

  def __str__(self):
    return '{} {} {}'.format(self.category, self.name, self.amount)

class PeriodExpenseAllotment(models.Model):
  name = models.CharField(max_length=100)
  default_allotment = models.DecimalField(max_digits=6, decimal_places=2)
  is_long_term = models.BooleanField()

  def __str__(self):
    return '{} {}'.format(self.name, self.default_allotment)


class PeriodExpense(models.Model):
  budget_period = models.ForeignKey(BudgetPeriod, on_delete=models.CASCADE)
  period_expense_allotment = models.ForeignKey(PeriodExpenseAllotment,
                                on_delete=models.CASCADE, null=True)
  amount = models.DecimalField(max_digits=6, decimal_places=2)

  def __str__(self):
    return 'Period: {} Allotment: {} Amount: {}'.format(self.budget_period, self.period_expense_allotment, self.amount)


class ExpenseSpent(models.Model):
  period_expense = models.ForeignKey(PeriodExpense, on_delete=models.CASCADE)
  date_spent = models.DateTimeField(auto_now_add=True)
  amount = models.DecimalField(max_digits=6, decimal_places=2)

  def __str__(self):
    return '{} {}'.format(self.period_expense, self.amount)


class Income(models.Model):
  budget_period = models.ForeignKey(BudgetPeriod, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  amount = models.DecimalField(max_digits=6, decimal_places=2)
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return '{} {}'.format(self.name, self.amount)
