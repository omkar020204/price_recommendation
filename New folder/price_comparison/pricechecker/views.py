# pricechecker/views.py
from django.shortcuts import render
from .forms import ProductSearchForm
from .utils import compare_prices

def index(request):
    form = ProductSearchForm()
    cheapest_price = None
    cheapest_site = None

    if request.method == 'POST':
        form = ProductSearchForm(request.POST)
        if form.is_valid():
            product_name = form.cleaned_data['product_name']
            cheapest_price, cheapest_site = compare_prices(product_name)

    return render(request, 'pricechecker/index.html', {
        'form': form,
        'cheapest_price': cheapest_price,
        'cheapest_site': cheapest_site
    })
