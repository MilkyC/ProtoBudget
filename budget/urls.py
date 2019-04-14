from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:budget_period_id>', views.index),
]
