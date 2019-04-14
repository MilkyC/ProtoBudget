from django.contrib import admin

# Register your models here.

from .models import Allotment, Budget, BudgetPeriod, Category, PeriodExpenseAllotment, PeriodExpense


class BudgetPeriodAdmin(admin.ModelAdmin):
  fields = ['budget', 'name', 'start_date', 'end_date']
  list_display = ('name',)
  
  def save_model(self, request, obj, form, change):
    super().save_model(request, obj, form, change)
    # Create Allotments
    categories = Category.objects.all()
    user_message = ''
    for cat in categories:
      allotment = Allotment(
        budget_period=obj,
        category=cat,
        amount=cat.default_allotment)
      allotment.save()
      user_message += 'Saved allotment: {}\n'.format(allotment)

    # Create Budget Period Expenses
    period_expense_allotments = PeriodExpenseAllotment.objects.all()
    for expense_allotment in period_expense_allotments :
      period_expense = PeriodExpense(
        budget_period=obj,
        period_expense_allotment=expense_allotment,
        amount=expense_allotment.default_allotment)
      period_expense.save()
      user_message += 'Saved period expense: {}\n'.format(period_expense)
    self.message_user(request, user_message)

class CategoryAdmin(admin.ModelAdmin):
  fields = ['name', 'default_allotment']
  list_display = ('name', 'default_allotment')


class PeriodExpenseAllotmentAdmin(admin.ModelAdmin):
  list_display = ('name', 'default_allotment', 'is_long_term')


admin.site.register(Allotment)
admin.site.register(Budget)
admin.site.register(BudgetPeriod, BudgetPeriodAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PeriodExpense)
admin.site.register(PeriodExpenseAllotment, PeriodExpenseAllotmentAdmin)
