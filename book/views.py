from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum
from .models import Expense
from .serializers import ExpenseSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all().order_by('-date')
    serializer_class = ExpenseSerializer

@api_view(['GET'])
def budget_status(request):
    total = Expense.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    status = "黒字" if total >= 0 else "赤字"
    return Response({"total": total, "status": status})
