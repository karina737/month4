from django.urls import path
from . import views


urlpatterns = [
    path('clothes/', views.all_clothes, name='all_clothes'),
    path('tom_ford/', views.tom_ford_clothes_views, name='tom_ford_clothes'),
    path('miu_miu/', views.miu_miu_clothes_views, name='miu_miu_clothes'),
]   