from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from cart.views import AddCart, CartView, Checkout, DecreaseCart, PaymentSuccess, RemoveCart, Payment, OrderSummary

app_name = 'cart'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addcart/<int:product_id>/', AddCart.as_view(), name='addcart'),   
    path('removecart/<int:product_id>/', RemoveCart.as_view(), name='removecart'),  
    path('decreasecart/<int:product_id>/', DecreaseCart.as_view(), name='decreasecart'),
    path('cartview/', CartView.as_view(), name='cartview'),
    path('checkout/', Checkout.as_view(), name='checkout'),
    path('order-summary/', OrderSummary.as_view(), name='ordersummary'),
    path('payment/', Payment.as_view(), name='payment'),
    path('success/', PaymentSuccess.as_view(), name='paymentsuccess'),
]

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)