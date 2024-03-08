from django.shortcuts import render
from .serializers import UserSerializer, CustomerSerializer, ProductSerializer, CartSerializer, OrderPlacedSerializer
from django.contrib.auth.models import User 
from rest_framework import viewsets 
from .models import Customer, Product, Cart, OrderPlaced
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class RegisterUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    
class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer 
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        # You can customize the behavior before saving the object
        serializer.save(user=self.request.user)
    
class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class CartViewset(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
    def perform_create(self, serializer):
        # You can customize the behavior before saving the object
        serializer.save(user=self.request.user)
    
class OrderPlacedViewset(viewsets.ModelViewSet):
    queryset = OrderPlaced.objects.all()
    serializer_class = OrderPlacedSerializer
    
    
    
    
