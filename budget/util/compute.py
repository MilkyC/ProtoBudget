from budget.models import Allotment, Budget, BudgetPeriod, Category, PeriodExpense

def compute_values(budget_period_id=None):
  return {**compute_monthly_total(budget_period_id)}

def compute_monthly_total(budget_period_id=None):
  if budget_period_id is None:
    budget_period = BudgetPeriod.objects.last()
  else:
    budget_period = BudgetPeriod.objects.get(pk=budget_period_id)

  budget_period_expenses = PeriodExpense.objects.filter(budget_period=budget_period)
  totals = {
    'long_term_total': 0,
    'monthly_total': 0,
  }
  for bpe in budget_period_expenses:
    if bpe.period_expense_allotment.is_long_term:
      totals['long_term_total'] += bpe.amount
    else:
      totals['monthly_total'] += bpe.amount

  return totals 
