from django import forms
from .models import Order

class OrderForm(forms.ModelForm):

    radio_choices = [
        ('cod', 'Cash On Delivery'), ('online', 'Online Payment'), 
    ]
    payment_method = forms.ChoiceField(
        choices=radio_choices,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Order
        fields = ['address', 'phone', 'payment_method']