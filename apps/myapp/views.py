from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def index(req):
    return render(req, 'myapp/index.html')


def register(req):
    results = User.objects.regValidator(req.POST)

    if results[0]:
        req.session['id'] = results[1].id
        req.session['name'] = results[1].fname
        return redirect('/dashboard')
    else:
        for error in results[1]:
            messages.add_message(req, messages.ERROR, error, extra_tags='register')
        return redirect('/')


def login(req):
    results = User.objects.loginValidator(req.POST)

    if results[0]:
        req.session['id'] = results[1].id
        req.session['name'] = results[1].fname
        return redirect('/dashboard/{}'.format(req.session['id']))
    else:
        for error in results[1]:
            messages.add_message(req, messages.ERROR, error, extra_tags='login')
        return redirect('/')


def sell(req):
    results = Product.objects.productValidator(req.POST, req.session['id'])
    return redirect('/dashboard/{}'.format(req.session['id']))


def shoes(req):
    context = {
        'all_products_for_sale': Product.objects.filter(isSold = False)
    }
    return render(req, 'myapp/shoes.html', context)


def buy(req, product_id):
    Sales.objects.create(product_id=product_id, buyer_id=req.session['id'])
    product = Product.objects.get(id=product_id)
    product.isSold = True
    product.save()
    return redirect('/shoes')


def logout(req):
    req.session.clear()
    return redirect('/')


def remove(req, product_id):
    Product.objects.get(id=product_id).delete()
    return redirect('/dashboard/{}'.format(req.session['id']))


def dashboard(req, user_id=None):
    my_sales = []
    inventory_total = 0
    sales_total = 0
    purchase_total = 0

    # === INVENTORY ===
    inventory = Product.objects.filter(seller_id = req.session['id'], isSold=False)

    for product in inventory:
        inventory_total += product.price


    # === SALES ===
    all_sales = Sales.objects.all()

    for sale in all_sales:
        if sale.product.seller_id == req.session['id']:
            my_sales.append(sale)

    for sale in my_sales:
        sales_total += sale.product.price


    # === PURCHASES ===
    purchases = Sales.objects.filter(buyer_id = req.session['id'])

    for purchase in purchases:
        purchase_total += purchase.product.price


    context = {
        'inventory' : inventory,
        'sales' : my_sales,
        'purchases' : purchases,
        'inventory_total' : inventory_total,
        'sales_total' : sales_total,
        'purchase_total' : purchase_total
    }

    return render(req, 'myapp/dashboard.html', context)
