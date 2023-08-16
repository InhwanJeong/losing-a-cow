from rest_framework import serializers

from service.models import KCACustomerDangerousData, Inference


class KCADataSerializer(serializers.ModelSerializer):
    class Meta:
        model = KCACustomerDangerousData
        fields = '__all__'


class InferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inference
        fields = '__all__'
