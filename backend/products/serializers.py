from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse
from .validators import validate_title
class ProductSerializer(serializers.ModelSerializer):
    my_discount=serializers.SerializerMethodField(read_only=True)
    edit_url =serializers.HyperlinkedIdentityField(
            view_name='product-update',
            lookup_field='pk'
    )
    title=serializers.CharField(validators=[validate_title])
    url = serializers.HyperlinkedIdentityField(
            view_name='product-detail',
            lookup_field='pk'
    )
    # email=serializers.EmailField(write_only=True)
    #     def validate_title(self, value):
    #     request = self.context.get('request')
    #     user = request.user
    #     qs = Product.objects.filter(user=user, title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name.")
    #     return value
    
    class Meta:
        model=Product 
        fields=[
            'user',
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount', 
        ]
    # def get_edit_url(self, obj):
    #     request = self.context.get('request') # self.request
    #     if request is None:
    #         return None
    #     return reverse("product-update", kwargs={"pk": obj.pk}, request=request) 
    # def create(self,validated_data):
    #     email=validated_data.pop('email')
    #     return super().create(validated_data)
    def get_my_discount(self,obj):
        if not hasattr(obj,'id'):
            return None
        if not isinstance(obj,Product):
            return None       
        return obj.get_discount()
       