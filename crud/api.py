from rest_framework.generics import ListAPIView
from models.models import Product, History
from .serializers import ProductSerializer, ProductFullSerializer


class AllProductView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        product_category = self.kwargs['category']
        queryset = Product.objects.filter(category=product_category)
        return queryset


class ProductFullView(ListAPIView):
    serializer_class = ProductFullSerializer

    def get_queryset(self):
        product_category = self.kwargs['category']
        product_id = self.kwargs['pk']
        queryset = Product.objects.filter(category=product_category, id=product_id)
        return queryset
