from rest_framework import serializers
from .models import Component_status

class Component_status_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Component_status
        fields = ('cid','status')

