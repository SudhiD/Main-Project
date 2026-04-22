from django.shortcuts import render,redirect
from .models import Cart, OrderItems
from shope.models import Products
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from cart.forms import OrderForm
from cart.models import Order
import razorpay
import uuid

# Create your views here.

class AddCart(View):
    def get(self,request,product_id):
        user = request.user
        product = Products.objects.get(id=product_id)
        try:
            c = Cart.objects.get(user=user, product=product)
            c.quantity += 1
            c.save()
        except Cart.DoesNotExist:
            Cart.objects.create(user=user, product=product, quantity=1)    
        return redirect('cart:cartview')
    
class CartView(View):
    def get(self,request):
        user = request.user
        items = Cart.objects.filter(user=user)
        total = 0
        for i in items:
            total += i.product.price * i.quantity
        context = {'items': items, 'total': total}
        
        return render(request,'cart.html',context)   

class DecreaseCart(View):
    def get(self,request,product_id):
        try:
            c = Cart.objects.get(id=product_id, user=request.user)
            if c.quantity > 1:
                c.quantity -= 1
                c.save()
            else:
                c.delete()
        except:
            pass
        return redirect('cart:cartview')
    
class RemoveCart(View):
    def get(self,request,product_id):
        try:
            c = Cart.objects.get(id=product_id)
            c.delete()
        except:
            pass
        return redirect('cart:cartview')  
    

class Payment(View):
    def get(self,request):
        return render(request,'payment.html')  

class Checkout(View):
    def post(self,request):
        form_instance = OrderForm(request.POST)
        if form_instance.is_valid():
            order = form_instance.save(commit=False)

            user = request.user
            order.user = user

            cart = Cart.objects.filter(user=user)
            total = 0
            for i in cart:
                total += i.product.price * i.quantity
            order.amount = total
            
            order.save()

            if order.payment_method == 'online':
                client = razorpay.Client(auth=('rzp_test_SeUkPwRXblu7kK', 'DwcqHCcViQ7JQP7IF2XrTsvP'))
                payment = client.order.create({'amount': order.amount*100, 'currency': 'INR'})
                print(payment)
                id = payment['id']
                order.order_id = id
                order.save()
                context = {'payment': payment}                             
                return render(request,'payment.html', context)                
            else:
                id = uuid.uuid4().hex[:14]
                i = 'cod_ORDER'+id
                order.order_id = i
                order.is_ordered = True
                order.save()

                cart = Cart.objects.filter(user=user)
                for i in cart:
                    OrderItems.objects.create(order=order, product=i.product, quantity=i.quantity)
                    i.delete()  
                return render(request,'payment.html')
    def get(self,request):
        form_instance = OrderForm()
        context = {'form': form_instance}
        return render(request,'checkout.html', context)    
    
@method_decorator(csrf_exempt, name='dispatch')    
class PaymentSuccess(View):
    def post(self,request):
        response = request.POST
        print(response)
        o = Order.objects.get(order_id=response['razorpay_order_id'])
        o.is_ordered = True
        o.save()

        items = Cart.objects.filter(user=o.user)
        for i in items:
            OrderItems.objects.create(order=o, product=i.product, quantity=i.quantity)
            i.delete()
             
        return render(request,'payment_success.html')    

class OrderSummary(View):   
    def get(self,request): 
        o = Order.objects.filter(user=request.user, is_ordered=True)
        return render(request,'order_summary.html', {'orders': o})  
