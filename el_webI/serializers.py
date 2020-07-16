from rest_framework import serializers
from .models import Component_data

class BoardInfoSerializer(serializers.Serializer):
    d1Stat = serializers.BooleanField(default=False)
    d2Stat = serializers.BooleanField(default=False)
    d3Stat = serializers.BooleanField(default=False)
    d4Stat = serializers.BooleanField(default=False)
    instantPower = serializers.FloatField(default=0)
    totalPower = serializers.FloatField(default=0)

class Component_status_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Component_data
        fields = ('boardNo','deviceNo','status','watt')

class Status_shifter_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Component_data
        fields = ( )
