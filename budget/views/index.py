from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from budget.models import Allotment, Budget, BudgetPeriod, Category, PeriodExpense
from budget.util.compute import compute_values

def index(request, budget_period_id=None):
  if budget_period_id is None:
    budget_period = BudgetPeriod.objects.last()
  else:
    budget_period = BudgetPeriod.objects.get(pk=budget_period_id)

  budget_period_expenses = PeriodExpense.objects.filter(budget_period=budget_period)

  category_list = Category.objects.all()
  context = {
      'budget_period_expenses': budget_period_expenses,
      'budget_period': budget_period,
      'categories': category_list,
      'computed_values': compute_values(budget_period_id),
  }
  return render(request, 'budget/index.html', context)
