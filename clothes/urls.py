from django.urls import path
from . import views


urlpatterns = [
    path('clothes/', views.AllClothesView.as_view(), name='all_clothes'),
    path('tom_ford/', views.TFClothesView.as_view(), name='tom_ford_clothes'),
    path('miu_miu/', views.MMClothesView.as_view(), name='miu_miu_clothes'),
]   