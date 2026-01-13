from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100, blank=True, default="")
    phone_number = models.CharField(max_length=15, default="+996")
    GENDER = (
        ('MALE', 'MALE'),
        ("FEMALE", "FEMALE")
    )
    gender = models.CharField(max_length=100, choices=GENDER)
    city = models.CharField(max_length=100)
    FORMAT = (
        ('OFFICE', 'OFFICE'),
        ('REMOTE', 'REMOTE'),
        ('HYBRID', 'HYBRID')
    )
    format= models.CharField(max_length=100, choices=FORMAT)
    LEVEL = (
        ('INTERN', 'INTERN'),
        (' JUNIOR', ' JUNIOR'),
        ('MIDDLE', 'MIDDLE'),
        (' SENIOR', ' SENIOR'),
    )
    level=models.CharField(max_length=100, choices=LEVEL)
    LANGUAGES= (
        ('PYTHON', 'PYTHON'),
        ('JAVA', 'JAVA'),
        ('GO', 'GO'),
        (' NODE', ' NODE'),
        (' CSHARP', ' CSHARP')
    )
    languages= models.CharField(max_length=100, choices=LANGUAGES)
    ENGLISHLEVEL = (
        ('A2', 'A2'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('C1', 'C1')
    )
    englishlevel=models.CharField(max_length=100, choices=ENGLISHLEVEL,  null=True,blank=True)
    years_experience = models.PositiveSmallIntegerField(
    validators=[MinValueValidator(0), MaxValueValidator(40)],
    default=0)
    resume_url = models.URLField(blank=True)
    about = models.TextField()
    consent = models.BooleanField( default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.username