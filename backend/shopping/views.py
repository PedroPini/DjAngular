from django.shortcuts import render
from rest_framework import viewsets

from .models import ShoppingItem, User
from .serializers import ShoppingItemSerializer, UserSerializer


class ShoppingItemViewSet(viewsets.ModelViewSet):

    serializer_class = ShoppingItemSerializer
    queryset = ShoppingItem.objects.all()
    
class UserViewSet(viewsets.ModelViewSet):
    
    serializer_class = UserSerializer
    queryset = User.objects.all()
