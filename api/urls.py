from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter(trailing_slash=False)
router.register('kca-data', views.KCADataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
