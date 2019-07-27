from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from datetime import datetime

# from django.core.files.storage import FileSystemStorage

# Create your views here.
def home(req):
    products = Product.objects.order_by('-votes_total') 

    return render(req, 'home.html', {'products':products})

@login_required(login_url='login_or_signup')
def create(req):
    if req.method=='POST':
        
        new_product = Product()
        # From the user
        new_product.title=req.POST['title']
        new_product.url=req.POST['url']
        new_product.body=req.POST['body']
        new_product.icon=req.FILES['thumbnail']
        new_product.image=req.FILES['poster']
        # Default
        new_product.pub_date=datetime.now()
        new_product.hunter=req.user
        new_product.votes_total=1
        new_product.upvoters=''
        new_product.save()
        return redirect('/products/'+str(new_product.id))
    else:    
        return render(req, 'create.html')

# def detail(req, product_id):
#     product= get_object_or_404(Product, pk=product_id)
#     return render(req, 'detail.html', {'product':product, 'disabled':''})

@login_required(login_url='login_or_signup')
def upvote(req, product_id):
    product= get_object_or_404(Product, pk=product_id)
    upvoters=product.upvoters.split()
    print(upvoters)
    if req.user == product.hunter:
        return render(req, 'detail.html', {'product':product, 'disabled':'disabled'})
    for voter in upvoters:
        if voter == req.user.username:
            return render(req, 'detail.html', {'product':product, 'disabled':'disabled'})
    if req.method=='POST':
        product.votes_total+=1
        print("Hello")
        product.upvoters += str(req.user.username)
        product.upvoters+= ' '
        product.save()
        return render(req, 'detail.html', {'product':product, 'disabled':'disabled'})
        # return redirect('/products/'+str(product.id))
    else:           
        return render(req, 'detail.html', {'product':product, 'disabled':' '})
