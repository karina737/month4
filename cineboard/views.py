from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import generic
from cineboard.models import Movie
from .models import SimpleRegisterForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from .forms import MovieCreateForm
from django.views.generic import DeleteView

class RegisterView(generic.CreateView):
    template_name = 'cineboard/register.html'
    form_class = SimpleRegisterForm
    success_url = "users:login"

class AuthLoginView(LoginView):
    template_name = 'cineboard/login.html'
    form_class = AuthenticationForm
    
    def get_success_url(self):
        return reverse("movie_list")

class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('home_page')

class MovieListView(generic.ListView):
    template_name = 'cineboard/movie_list.html'
    context_object_name = 'cinema'
    model = Movie
    login_url = None

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class MovieCreateView(generic.CreateView):
    template_name = "cineboard/movie_create.html"
    model = Movie
    form_class = MovieCreateForm
    success_url = reverse_lazy("cineboard:movie_success")


class MovieSuccessView(generic.TemplateView):
    template_name = "cineboard/movie_success.html"


class MovieDetailView(generic.DetailView):
    template_name = "cineboard/movie_detail.html"
    model = Movie
    context_object_name = "movie"


class MovieUpdateView(generic.UpdateView):
    template_name = 'cineboard/update_movie.html'
    model = Movie
    form_class = MovieCreateForm
    success_url = reverse_lazy("cineboard:movie_success")

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        return get_object_or_404(Movie, id=id)
    
class MovieDeleteView(generic.DeleteView):
    model = Movie
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('cineboard:movie_list')