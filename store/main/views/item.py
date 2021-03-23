from django.shortcuts import render
from rest_framework import viewsets
from main.models import Item
from main.serializers import ItemSerializer

# Create your views here.


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
