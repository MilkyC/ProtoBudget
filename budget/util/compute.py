from budget.models import Allotment, Budget, BudgetPeriod, Category, ComputedValue, PeriodExpense

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=PeriodExpense)
def compute_values_callback(sender, **kwargs):
  compute_values()

def compute_values(budget_period_id=None):
  return {**compute_monthly_total(budget_period_id),
          **compute_allotment_total(budget_period_id)}

def compute_allotment_total(budget_period_id=None):
  if budget_period_id is None:
    budget_period = BudgetPeriod.objects.last()
  else:
    budget_period = BudgetPeriod.objects.get(pk=budget_period_id)

  allotments = Allotment.objects.filter(budget_period=budget_period)
  previous_budget_period = budget_period.id - 1
  previous_allotments = Allotment.objects.filter(budget_period=previous_budget_period)
  allotment_totals = {}
  for allotment in allotments:
    curr_name = 'allotment_total_' + str(allotment.id)
    allotment_totals[curr_name] = allotment.amount
    for prev_allotment in previous_allotments:
      if allotment.category.name == prev_allotment.category.name:
        allotment_totals[curr_name] += prev_allotment.amount

  return allotment_totals
 
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

  for key in totals:
    try:
      comp_val = ComputedValue.objects.get(
        budget_period=budget_period,
        name=key)
    except:
      comp_val = ComputedValue()
      comp_val.budget_period = budget_period
      comp_val.name=key

    if comp_val.amount != totals[key]:
      comp_val.amount = totals[key]
      comp_val.save()

  return totals 
