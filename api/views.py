from rest_framework import viewsets

from api.serializers import KCADataSerializer, InferenceSerializer
from service.models import KCACustomerDangerousData, Inference


class KCADataViewSet(
    viewsets.GenericViewSet,
    viewsets.mixins.CreateModelMixin,
):
    queryset = KCACustomerDangerousData.objects.all()
    serializer_class = KCADataSerializer


class InferenceViewSet(
    viewsets.GenericViewSet,
    viewsets.mixins.CreateModelMixin,
):
    queryset = Inference.objects.all()
    serializer_class = InferenceSerializer
