from django.shortcuts import render
from .models import product
# from django.http import HttpResponse
# Create your views here.

# def index(request):
#     return HttpResponse("<h1>My First Webpage with python Django<h1/>")

def product_list(request):
    products = product.objects.all()
    context ={
        'products' : products
    }
    return render(request,'plp_ecommerce/product_list.html',context)


# def product_list(request):
#     try:
#         template = loader.get_template('plp_ecommerce/product_list.html')
#     except TemplateDoesNotExist:
#         print(f"Template 'plp_ecommerce/product_list.html' not found. Checked directories:")
#         print(settings.TEMPLATES[0]['DIRS'])  # Adjust index based on your settings structure
#         raise
#     return HttpResponse(template.render(context, request))