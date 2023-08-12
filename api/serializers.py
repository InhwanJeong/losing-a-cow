from rest_framework import serializers

from service.models import KCACustomerDangerousData


class KCADataSerializer(serializers.ModelSerializer):
    class Meta:
        model = KCACustomerDangerousData
        fields = '__all__'
