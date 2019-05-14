from django import template

register = template.Library()

@register.inclusion_tag('budget/editable_expense.html')
def editable_period_expense(period_expense):
  return {
    'period_expense': period_expense,
  }

@register.inclusion_tag('budget/computed_value.html')
def computed_value(key, value):
  return {
    'key': key,
    'value': value,
  }
