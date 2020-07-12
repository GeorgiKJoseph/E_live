from rest_framework import serializers
from .models import Component_data

class Component_status_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Component_data
        fields = ('cid','status','current')

class Status_shifter_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Component_data
        fields = ( )
