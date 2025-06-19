from django.db import models

# Create your models here.

# モデルの定義
class Expence(models.Model):
    name = models.CharField(max_length=100) # 項目名
    amount = models.DecimalField(max_digits=10, decimal_places=2)   # 金額
    recorded_at = models.DateTimeField(auto_now_add=True)   # 記録日時