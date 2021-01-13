from django.conf.urls import url
from .api import ProductView, ProductFullView, AllProductView

urlpatterns = [
    url(r'v1/api/(?P<category>.+)/(?P<pk>[0-9]+)/$', ProductFullView.as_view(), name='ProductFullView'),
    url(r'v1/api/(?P<category>.+)/$', ProductView.as_view(), name='ProductView'),
    url(r'v1/api/$', AllProductView.as_view(), name='AllProductView'),
]