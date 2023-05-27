from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .models import Product, Collection, Review
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer, CollectionSerializer, ReviewSerializer
# Create your views here.

####### USING VIEW-SET METHODS ######################################
############for [GET, POST,PUT, PATCH, DELETE] ########################
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


#using GENERIC VIEW SET METHODS ######################################
############for create and post [GET, POST] #########################

# class ProductList(ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    

############for[GET, PUT, DELETE] #########################
# class ProductDetails(RetrieveUpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
#     def delete(self, request, pk):
#         product = get_object_or_404(Product, pk=pk)
#         if product.orderitems.count() > 0:
#             return Response({'error': 'product can not be deleted it is associated with other...'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
############## [CLASS BASED VIEW METHODS ]#################################################################
# class ProductList(APIView):
#     def get(self, request):
#         queryset = Product.objects.all()
#         serializer = ProductSerializer(queryset, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

############TO GER DETAILS AND ONE #################################################################

# class ProductDetails(APIView):
#     def get(self, request, id):
#         product = get_object_or_404(Product, pk=id) 
#         serializer = ProductSerializer(product)
#         return Response(serializer.data) 
#     def put(self, request, id):
#         product = get_object_or_404(Product, pk=id)
#         serializer = ProductSerializer(product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
 
#     def delete(self, request, id):
#         product = get_object_or_404(Product, pk=id)
#         if product.orderitems.count() > 0:
#             return Response({'error': 'product can not be deleted it is associated with other...'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


####### USING VIEW-SET METHODS ######################################
############for [GET, POST,PUT, PATCH, DELETE] ########################   
class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    

#building collection end point
################ USING GENERIC VIEW METHOD FOR COLLECTION METHOD #############################
class CollectionList(ListCreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    
    
################ USING FUNCTION BASED VIEW METHOD FOR COLLECTION METHOD #############################    
# @api_view(['GET', 'POST'])
# def collection_list(request):
#     if request.method == 'GET':
#         queryset = Collection.objects.all()
#         serializer = CollectionSerializer(queryset, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CollectionSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

##### FUNCTION BASED METHOD ####### 

# @api_view(['GET', 'PUT', 'DELETE'])
# def collection_details(request, pk):
#     collection = get_object_or_404(Collection, pk=pk)
#     if request.method=='GET':
#         serializer = CollectionSerializer(collection)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = CollectionSerializer(collection, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     elif request.method == 'DELETE':
#         collection.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


################ REVIEW SECTION #################################
class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer