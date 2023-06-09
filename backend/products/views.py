from rest_framework import authentication,generics,mixins,permissions
from .models import Product
from api.mixins import StaffEditorPermissionMixin,UserQuerySetMixin
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.permissions import IsStaffEditorPermission
from api.authentication import TokenAuthentication
class ProductListCreateAPIView(
    # StaffEditorPermissionMixin,
    UserQuerySetMixin,
    generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    # permission_classes=[permissions.IsAdminUser,isStaffEditorPermission]
    def perform_create(self,serializer):
      # serializer.save(user=self.request.user)
      #  print(serializer.validated_data)
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        if content is None:
            content=title
        serializer.save(user=self.request.user,content=content)
    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     user = request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     print(request.user)
    #     return qs.filter(user=request.user)        
product_list_create_view=ProductListCreateAPIView.as_view()



class ProductDetailAPIView(
    # StaffEditorPermissionMixin,
    UserQuerySetMixin,
    generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

product_detail_view=ProductDetailAPIView.as_view()



class ProductUpdateAPIView(
    # StaffEditorPermissionMixin,
    UserQuerySetMixin,
    generics.UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'
    def perform_update(self,serializer):
        instance=serializer.save()
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        if content is None:
            content=title
product_update_view=ProductUpdateAPIView.as_view()



class ProductDestroyAPIView(
    # StaffEditorPermissionMixin,
    UserQuerySetMixin,
    generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # instance 
        super().perform_destroy(instance)

product_delete_view = ProductDestroyAPIView.as_view()













# class ProductListAPIView(generics.ListAPIView):
#     queryset=Product.objects.all()
#     serializer_class=ProductSerializer

# product_list_view=ProductDetailAPIView.as_view()

# class ProductMixinView(
#     mixins.CreateModelMixin,
#     mixins.ListModelMixin,
#     mixins.RetrieveModelMixin,
#     generics.GenericAPIView,
#     mixins.UpdateModelMixin,  
#     mixins.DestroyModelMixin,
#     ):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'pk'
#     def get(self, request, *args, **kwargs): #HTTP -> get
#         pk = kwargs.get("pk")
#         if pk is not None:
#             return self.retrieve(request, *args, **kwargs)
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):  
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs): 
#         return self.destroy(request, *args, **kwargs)
#     def perform_create(self, serializer):
#         # serializer.save(user=self.request.user)
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content') or None
#         if content is None:
#             content = "this is a single view doing cool stuff"
#         serializer.save(content=content)

#     # def post(): #HTTP -> post

# product_mixin_view = ProductMixinView.as_view()












# @api_view(['GET', 'POST'])
# def product_alt_view(request, pk=None, *args, **kwargs):
#     method = request.method 

#     if method == "GET":
#         if pk is not None:
#             # detail view
#             obj = get_object_or_404(Product, pk=pk)
#             data = ProductSerializer(obj, many=False).data
#             return Response(data)
#         # list view
#         queryset = Product.objects.all() 
#         data = ProductSerializer(queryset, many=True).data
#         return Response(data)

#     if method == "POST":
#         # create an item
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             title = serializer.validated_data.get('title')
#             content = serializer.validated_data.get('content') or None
#             if content is None:
#                 content = title
#             serializer.save(content=content)
#             return Response(serializer.data)
#         return Response({"invalid": "not good data"}, status=400)