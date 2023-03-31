from rest_framework import serializers
from .models import FoodDb


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodDb
        fields = ('name', 'description')
