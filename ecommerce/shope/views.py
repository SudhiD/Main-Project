from django.shortcuts import render, redirect
from django.views import View
from shope.models import Category,Products
from shope.forms import CategoryForm, ProductsForm ,StockForm

# Create your views here.

class Categories(View):
    def get(self,request):
        c = Category.objects.all()
        context = {'categories': c}
        return render(request,'categoriesview.html',context)
    
class ProductsList(View):
    def get(self,request,category_id):
        category = Category.objects.get(id=category_id)
        context = {'category': category}
        return render(request,'products.html',context)   

class AddCategory(View):
    def get(self,request):
        form = CategoryForm()
        context = {'forms': form}
        return render(request,'addcategory.html',context)

    def post(self,request):
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shope:categories')
        context = {'forms': form}
        return render(request,'addcategory.html',context)    

class AddProduct(View):
    def get(self,request):
        form = ProductsForm()
        context = {'forms': form}
        return render(request,'addproducts.html',context)

    def post(self,request):
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shope:categories')
        context = {'forms': form}
        return render(request,'addproducts.html',context)     

class DetailProduct(View):
    def get(self,request,product_id):
        product = Products.objects.get(id=product_id)
        context = {'product': product}
        return render(request,'detailproduct.html',context)
    

class AddStock(View):    
    def get(self,request,product_id):
        product = Products.objects.get(id=product_id)
        form = StockForm(instance=product)
        context = {'forms': form}
        return render(request,'addstock.html',context)
    def post(self,request,product_id):
        product = Products.objects.get(id=product_id)
        form = StockForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
        return redirect('shope:detailproduct', product_id=product_id)      
    
from django.db.models import Q    

class Search(View):
    def get(self,request):
        query = request.GET.get('q') 
        products = Products.objects.filter(Q(name__icontains=query) | 
                                            Q(description__icontains=query) |
                                            Q(price__icontains=query) |
                                            Q(stock__icontains=query)
                                        )
        context = {'products': products, 'query': query}
        return render(request,'search.html',context)      

