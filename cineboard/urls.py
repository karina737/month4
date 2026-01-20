from django.urls import path
from . import views

app_name = "cineboard"

urlpatterns = [
    path("register/",views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path('', views.MovieListView.as_view(), name='movie_list'),
    path('create/', views.MovieCreateView.as_view(), name='movie_create'),
    path('success/', views.MovieSuccessView.as_view(), name='movie_success'),
    path('movie/<int:id>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('movie/<int:id>/delete/', views.MovieDeleteView.as_view(), name='movie_delete'),
    path('movie/<int:id>/update/', views.MovieUpdateView.as_view(), name='movie_update'),

]