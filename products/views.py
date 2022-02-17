from django.shortcuts import render
from products.models import Product
from django.core.paginator import Paginator
from django.db.models import Q

def shop(request,getCategory):
    products=Product.objects.all()
    if getCategory==0:
        getCategory='all'

    if getCategory==1:
        getCategory='women'
        products=products.filter(category=getCategory)

    elif getCategory==2:
        getCategory='men'
        products=products.filter(category=getCategory)

    elif getCategory==3:
        getCategory='kids'
        products=products.filter(category=getCategory)
    else:
        pass

    minamount,maxamount,size,color=22,99,[],[]
    if 'category' in request.GET:
        getCategory=request.GET['category']
        if getCategory=='all':
            pass
        else:
            category,kind=getCategory.split() 
            if category =='all':
                products=products.filter(type=kind)
            else:   
                products=products.filter(category=category,type=kind)
    if 'maxamount' in request.GET and 'minamount' in request.GET:
        maxamount=int(request.GET['maxamount'][1:])
        minamount=int(request.GET['minamount'][1:])
        products=products.filter(Q(price__gte=minamount,price__lte=maxamount)|Q(PriceAfterDiscount__gte=minamount,PriceAfterDiscount__lte=maxamount) )
        
    if 'size' in request.GET:
        size=request.GET.getlist('size')
        pattern='|'.join([i for i in size])
        products=products.filter(size__regex=f"{pattern}")
    if 'color' in request.GET:
        color=request.GET.getlist('color')
        pattern='|'.join([i for i in color])    
        products=products.filter(color__regex=f"{pattern}")

    paginator = Paginator(products,9) # Show 9 productss per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'shop/shop.html',{'page_obj': page_obj,'getCategory':getCategory,
                                            'maxValue':str(maxamount),'minValue':str(minamount),
                                            'size':size,'color':color})


def product_details(request,pro_id):
    product=Product.objects.get(id=pro_id)
    print(product)
    return render(request,'shop/product_details.html',{'pro':product})