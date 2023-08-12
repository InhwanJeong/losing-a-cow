from rest_framework import viewsets

from api.serializers import KCADataSerializer
from service.models import KCACustomerDangerousData


class KCADataViewSet(
    viewsets.GenericViewSet,
    viewsets.mixins.CreateModelMixin,
):
    queryset = KCACustomerDangerousData.objects.all()
    serializer_class = KCADataSerializer
