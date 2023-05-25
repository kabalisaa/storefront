from django.shortcuts import render
from django.http import HttpResponse
from store.models import Order, OrderItem, OrderItem, Product, Customer, Collection

# Create your views here.
def say_hello(request):
    
 
    
    return render(request, 'index.html',) #mapping  views with templates
    #return HttpResponse("hello world!") #mapping only views 
