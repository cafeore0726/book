from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum

from .models import Expence
from .serializers import ExpenceSerializer

# Create your views here.

class ExpenceViewSet(viewsets.ModelViewSet):
    queryset = Expence.objects.all()  # 全てのExpenceオブジェクトを取得
    serializer_class = ExpenceSerializer # シリアライザを指定
    
    @api_view(['GET']) # 合計金額を取得するエンドポイント
    def total_expence(request):
        total = Expence.objects.aggregate(Sum('amount'))['amount__sum'] or 0
        status = "黒字" if total >= 0 else "赤字" # 状態を判定
        return Response({"total":total, "status": status})  # 合計金額と状態を返す