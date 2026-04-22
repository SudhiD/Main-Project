from django.shortcuts import render,redirect
from django.views import View
from .forms import RegisterForm,LoginForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.

class Register(View):
    def get(self,request):
        forms = RegisterForm()
        return render(request,'register.html',{'forms':forms})
    def post(self,request):
        forms = RegisterForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('account:login')
        return render(request,'register.html',{'forms':forms})    

class Login(View):
    def get(self,request):
        forms = LoginForm()
        return render(request,'login.html',{'forms':forms})
    def post(self,request):
        forms = LoginForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            password = forms.cleaned_data['password']
            user = authenticate(request,username=name,password=password)
            if user:
                login(request,user)
                return redirect('shope:categories')
        return render(request,'login.html',{'forms':forms})
    
class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('account:login')    
  

