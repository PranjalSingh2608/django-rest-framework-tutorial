import json
from products.models import Product
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer
@api_view(['POST'])
def api_home(request,*args,**kwargs):
    """
    DRF API VIEW
    """
    # instance=Product.objects.all().order_by("?").first()
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance=serializer.save()
        # print(instance)
        data=serializer.data
    # if instance:
    #     # data=model_to_dict(model_data,fields=['id','title','content','sale_price'])
    #     data=ProductSerializer(instance).data
        return Response(serializer.data)
    return Response({"invalid":"not good data"},status=400)