from django.urls import path
from . import views

urlpatterns = [
    path('create_basket/', views.CreateBascetView.as_view(), name='create_basket'),
    path('basket_list/', views.ReadBasketView.as_view(), name='basket_list'),
    path('basket_list/<int:id>/update/', views.UpdateBasketView.as_view(), name='update'),
    path('basket_list/<int:id>/delete/', views.DeleteBasketView.as_view(), name='delete'),
]