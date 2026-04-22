from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.help_text = None    
    
class LoginForm(forms.Form):
    name = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)