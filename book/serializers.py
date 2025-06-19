from rest_framework import serializers
from .models import Expence


class ExpenceSerializer(serializers.ModelSerializer):
    # シリアライザの定義
    class Meta:
        model = Expence # シリアライズするモデル
        fields = '__all__'  # 全てのフィールドをシリアライズする