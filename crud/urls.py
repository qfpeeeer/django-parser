from django.conf.urls import url
from .api import ProductView, ProductFullView, AllProductView, MaxProductView, MinProductView

urlpatterns = [
    url(r'v1/api/(?P<category>.+)/maxprice/$', MaxProductView.as_view(), name='MaxProductView'),
    url(r'v1/api/(?P<category>.+)/minprice/$', MinProductView.as_view(), name='MinProductView'),
    url(r'v1/api/(?P<category>.+)/(?P<pk>[0-9]+)/$', ProductFullView.as_view(), name='ProductFullView'),
    url(r'v1/api/(?P<category>.+)/$', ProductView.as_view(), name='ProductView'),
    url(r'v1/api/$', AllProductView.as_view(), name='AllProductView'),
]