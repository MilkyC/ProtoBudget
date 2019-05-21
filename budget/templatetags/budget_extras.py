from django import template

register = template.Library()

@register.filter(name='addstr')
def addstr(arg1, arg2):
  """concatenate arg1 & arg2"""
  return str(arg1) + str(arg2)

@register.filter(name='lookup')
def lookup(value, arg):
  return value[arg]

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
