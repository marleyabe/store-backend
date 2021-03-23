"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from main.views.product import ProductViewSet
from main.views.category import CategoryViewSet
from main.views.subcategory import SubCategoryViewSet
from main.views.item import ItemViewSet

router = routers.DefaultRouter()

router.register(r'product', ProductViewSet, basename="Product")
router.register(r'category', CategoryViewSet, basename="Category")
router.register(r'subcategory', SubCategoryViewSet, basename="SubCategory")
router.register(r'item', ItemViewSet, basename="item")

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

]
