from rest_framework import serializers
from .models import hostelsportsequipment

class hostelsportsequipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=hostelsportsequipment
        fields='__all__'