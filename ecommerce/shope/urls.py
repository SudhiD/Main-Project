"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from shope.views import AddStock, Categories, DetailProduct,  AddCategory, AddProduct, ProductsList,Search

app_name = 'shope'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Categories.as_view(), name='categories'),
    path('products/<int:category_id>/', ProductsList.as_view(), name='products'),
    path('addcategory/', AddCategory.as_view(), name='addcategory'),
    path('addproduct/', AddProduct.as_view(), name='addproduct'),
    path('detailproduct/<int:product_id>/', DetailProduct.as_view(), name='detailproduct'),
    path('addstock/<int:product_id>/', AddStock.as_view(), name='addstock'),
    path('search/', Search.as_view(), name='search'),    
]

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)