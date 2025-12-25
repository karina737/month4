from django.urls import path
from . import views

urlpatterns = [
    path('ex_1/', views.top_5_food_korea),
    path('ex_2/', views.timestamp),
    path('ex_3/', views.about_me),
]