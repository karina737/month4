from django.urls import path
from . import views

urlpatterns = [
    path("", views.categories_view, name="home"), 
    path("categories/", views.categories_view, name="categories"),
    path("products/", views.products_view, name="products"),
    path("categories/<int:category_id>/", views.category_products_view, name="category_products"),
]
