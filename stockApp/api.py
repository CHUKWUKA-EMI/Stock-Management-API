from rest_framework import viewsets, permissions
from .models import Stock
from .serializer import StockSerializer

# Create your views here.
class StockViewSet(viewsets.ModelViewSet):
  queryset = Stock.objects.all()
  permission_classes =[
    permissions.AllowAny
  ]
  serializer_class = StockSerializer