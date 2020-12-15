from rest_framework import serializers
from vin.models import Vin


class VinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vin
        fields = ['variable', 'variableId', 'value', 'valueId']
