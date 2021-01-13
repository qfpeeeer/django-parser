from django.conf.urls import url
from django.urls import path, include

from .api import PhoneViewSet, LaptopViewSet, KeyboardViewSet, MonitorViewSet, PhonesHistoryView, PhoneInfoView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('phone', PhoneViewSet, 'phone')
router.register('laptop', LaptopViewSet, 'laptop')
router.register('keyboard', KeyboardViewSet, 'keyboard')
router.register('monitor', MonitorViewSet, 'monitor')

urlpatterns = [
    url(r'api/phone_price_history/(?P<pk>[0-9]+)/$', PhonesHistoryView.as_view(), name='PhonesHistoryView'),
    url(r'api/phone_full/(?P<pk>[0-9]+)/$', PhoneInfoView.as_view(), name='PhoneInfoView'),
    path('api/', include(router.urls)),
]

urlpatterns += router.urls
