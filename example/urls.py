from django.conf.urls import url
from django.urls import path, include

from .api import PhoneViewSet, LaptopViewSet, KeyboardViewSet, MonitorViewSet, PhonesView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('phone', PhoneViewSet, 'phone')
router.register('laptop', LaptopViewSet, 'laptop')
router.register('keyboard', KeyboardViewSet, 'keyboard')
router.register('monitor', MonitorViewSet, 'monitor')

urlpatterns = [
    url(r'api/phoneinfo/(?P<pk>[0-9]+)/$', PhonesView.as_view(), name='phoneOne'),
    path('api/', include(router.urls)),
]

urlpatterns += router.urls
