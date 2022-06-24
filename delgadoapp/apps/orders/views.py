from ast import Or
from django.shortcuts import render, get_object_or_404, redirect
from .forms import OrderItemForm
from .models import OrderItem

def list_orders(request):
    template_name = 'orders/list_orders.html'
    orders = OrderItem.objects.filter()
    # order_items = OrderItem.objects.filter()
    # products = Product.objects.filter()
    # clients = Client.objects.filter()
    context = {
        'orders': orders,
        # 'order_items': order_items,
        # 'products': products,
        # 'clients': clients
    }
    return render(request, template_name, context)

def add_order_item(request):
    template_name = 'orders/add_order_item.html'
    context = {}
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('orders:list_orders')
    form = OrderItemForm()
    context['form'] = form
    return render(request, template_name, context)

def delete_order_item(request, id_order_item):
    orderitem = OrderItem.objects.get(id=id_order_item)
    orderitem.delete()
    return redirect('orders:list_orders')

def edit_order_status(request, id_order):
    template_name = 'orders/add_order_item.html'
    context ={}
    order = get_object_or_404(OrderItem, id=id_order)
    if request.method == 'POST':
        form = OrderItemForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders:list_orders')
    form = OrderItemForm(instance=order)
    context['form'] = form
    return render(request, template_name, context)