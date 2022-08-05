from django.shortcuts import render
from .models import Product


# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # here we pass properties one by one
    # context = {
    #     'title': obj.title,
    #     'summary': obj.summary,
    #     'description': obj.description,
    #     'price': obj.price
    # }
    # and here we pass the whole object so if we will update it we shouldn't at least edit the view
    context = {'object':obj}
    return render(request, 'products/product_detail.html', context)