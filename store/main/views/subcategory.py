from django.shortcuts import render
from rest_framework import viewsets
from main.models import SubCategory
from main.serializers import SubCategorySerializer

# Create your views here.


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
