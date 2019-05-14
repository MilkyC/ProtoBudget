from budget.models import Category
from rest_framework import viewsets
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
