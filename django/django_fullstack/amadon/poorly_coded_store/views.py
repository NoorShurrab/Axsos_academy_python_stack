# Handles displaying products, processing purchases, and
# showing checkout/order summary information
from django.shortcuts import render, redirect
from .models import Order, Product

# Displays all available products
def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

# Calculates the total charge, creates an Order record, stores the latest purchase info in the session, then redirects to checkout.
def buy(request):
    if request.method != "POST":
        return redirect('/')

    product_id = request.POST.get('product_id')
    quantity = int(request.POST.get('quantity', 1))

    product_query = Product.objects.filter(id=product_id)

    if product_query.exists():
        product = product_query.first()
        
        charge = product.price * quantity # Calculate total charge for this purchase
        
        Order.objects.create( # Record the order in the database
            quantity_ordered=quantity, 
            total_price=charge
        )
        # Save the latest purchase info in the session
        request.session['last_charge'] = "{:.2f}".format(charge)
        request.session['last_quantity'] = quantity
        
        request.session.modified = True
        
        return redirect('/checkout/')
        
    else:
        return redirect('/') # Invalid product id - redirect back to home

# Displays checkout page with the last purchase details and overall totals across all orders
def checkout(request):
    all_orders = list(Order.objects.iterator())
    total_quantity = 0
    total_spent = 0

    # Sum up quantities and totals from all past orders
    for order in all_orders:
        total_quantity += order.quantity_ordered
        total_spent += order.total_price

    context = {
        'last_charge': request.session.get('last_charge', '0.00'),
        'last_quantity': request.session.get('last_quantity', 0),
        'total_quantity': total_quantity,
        'total_spent': "{:.2f}".format(total_spent),
    }
    return render(request, "store/checkout.html", context)