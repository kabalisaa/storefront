from django.urls import path
#from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers
from . import views

router =routers.DefaultRouter()
router.register('product', views.ProductViewSet)
router.register('collection', views.CollectionViewSet)

products_router=routers.NestedDefaultRouter(router, 'product', lookup='productt')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')

urlpatterns = router.urls + products_router.urls


##### FOR FUNCTIONAL, CLASSS AND GENERIC BASED VIEW __#############

# urlpatterns = [
#     path('product/', views.ProductList.as_view()),
#     path('product/<int:pk>/', views.ProductDetails.as_view()),
    
#     path('collection/', views.CollectionList.as_view()),
#     path('collection/<int:pk>/', views.collection_details),
# ]
