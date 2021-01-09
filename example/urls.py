from django.urls import path
from . import views
from rest_framework import routers
from .api import DataViewSet

router = routers.DefaultRouter()
router.register('api/example', DataViewSet, 'example')

urlpatterns = router.urls