from django.shortcuts import render

# Create your views here.

def home(request):
  return render(request, 'index.html')

def login(request):
  return render(request, 'login.html')

def pizzas(request): 
  return render(request, 'tabela-pizzas.html')

def restaurantes(request): 
  return render(request, 'blank-page.html')

def register(request): 
  return render(request, 'register.html')