from django.shortcuts import render
from products.models import Product

def index(request):
    menItems=len(Product.objects.filter(category='men'))
    kidsItems=len(Product.objects.filter(category='kids'))
    return render(request,'main/index.html',{'menItems':menItems,'kidsItems':kidsItems})