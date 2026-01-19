from django.shortcuts import render, get_object_or_404
from myShop.forms import CategoryForms, ProductForms
from myShop.models import Category, Product
from django.views import generic

def categories_view(request):
    categories = Category.objects.all()
    return render(request, "category/categories.html", {"categories": categories})


def products_view(request):
    products = Product.objects.select_related("category").all()
    return render(request, "category/products.html", {"products": products})

def category_products_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category).select_related("category")
    return render(request, "category/category_products.html", {
        "category": category,
        "products": products
    })
