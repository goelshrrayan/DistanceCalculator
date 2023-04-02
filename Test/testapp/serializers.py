from rest_framework import serializers
from .models import *


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        name = Shop
        model = Shop
        fields="__all__"
        # exclude = ["id"]  
     