from rest_framework import serializers
from store.models import Product, Collection, Review
from decimal import Decimal

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title','description', 'price', 'inventory', 'price_with_tax']
        #fields = '__all__'  #do not use all this is for lazy developer    
    price_with_tax= serializers.SerializerMethodField(method_name='calculate_tax') 
    def calculate_tax(self, product: Product):
        return product.price * Decimal(1.1)
    # def validate(self, data):
    #     if data['password'] != data['confirm_password']:
    #         return serializers.ValidationError('password do not match! ')
    #     return data

class CollectionSerializer(serializers.ModelSerializer):
        class Meta:
            model = Collection
            fields = ['id', 'title']


########### serializers for review #################################

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'date', 'name', 'description', 'product']
        