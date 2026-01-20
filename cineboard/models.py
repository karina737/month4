from django.db import models

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class SimpleRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username",)
        
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField("Название", max_length=200, unique=True)
    description = models.TextField("Описание")
    release_date = models.DateField("Дата выхода")
    GENRES = [
        ("action", "Боевик"),
        ("comedy", "Комедия"),
        ("drama", "Драма"),
        ("horror", "Ужасы"),
        ("fantasy", "Фэнтези"),
        ("sci-fi", "Фантастика"),
        ("other", "Другое"),
    ]
    genres = models.CharField("Жанр", max_length=30, choices=GENRES)
    rating = models.DecimalField("Рейтинг", max_digits=3, decimal_places=1, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name="movies")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
