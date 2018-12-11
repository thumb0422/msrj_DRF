from goods.models import ProductInfo
from rest_framework import viewsets
from goods.serializers import ProductInfoSerializer
from msrj.dbPool import session

# def goods(request):
#     return Response('000001')

class ProductInfoViewSet(viewsets.ModelViewSet):
    queryset = session.query(ProductInfo).order_by(ProductInfo.create_date)
    serializer_class = ProductInfoSerializer