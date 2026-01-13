from django import forms
from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import CaptchaField

GENDER = (
        ('MALE', 'MALE'),
        ("FEMALE", "FEMALE")
    )
FORMAT = (
        ('OFFICE', 'OFFICE'),
        ('REMOTE', 'REMOTE'),
        ('HYBRID', 'HYBRID')
    )
LEVEL = (
        ('INTERN', 'INTERN'),
        (' JUNIOR', ' JUNIOR'),
        ('MIDDLE', 'MIDDLE'),
        (' SENIOR', ' SENIOR'),
    )
LANGUAGES= (
        ('PYTHON', 'PYTHON'),
        ('JAVA', 'JAVA'),
        ('GO', 'GO'),
        (' NODE', ' NODE'),
        (' CSHARP', ' CSHARP')
    )
ENGLISHLEVEL = (
        ('A2', 'A2'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('C1', 'C1')
    )
class CustomRegisterForm(UserCreationForm):
    full_name= forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, initial='+996', required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    city = forms.CharField(max_length=100, required=True)
    format= forms.ChoiceField(choices=FORMAT, required=True)
    level= forms.ChoiceField(choices=LEVEL, required=True)
    languages= forms.ChoiceField(choices=LANGUAGES, required=True)
    englishlevel= forms.ChoiceField(choices=ENGLISHLEVEL, required=True)
    years_experience=forms.CharField(required=True)
    resume_url=forms.URLField(required=True)
    about = forms.CharField()
    consent=forms.BooleanField(required=True)
    created_at = forms.DateTimeField(required=False, disabled=True)


    class Meta:

       model = CustomUser
       fields = (
        "full_name",
        "email",
        "phone_number",
        "city",
        "gender",
        "format",
        "level",
        "languages",
        "years_experience",
        "resume_url",
        "englishlevel",
        "about",
        "consent",
        "password1",
        "password2",
    
        )
    def save(self, commit = True):
        user = super(CustomRegisterForm, self).save(commit=False)
        user.phone_number = self.cleaned_data['phone']
        if commit:
            user.save()
        return user
    
class CaptchaAuthenticationForm(AuthenticationForm):
    captcha = CaptchaField()