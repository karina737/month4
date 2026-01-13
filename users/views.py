
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .models import CustomUser
from .forms import CaptchaAuthenticationForm
from django.contrib.auth.models import Group

def candidate_apply_view(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name", "").strip()
        phone_number = request.POST.get("phone_number", "").strip()
        username = phone_number.replace("+", "").replace(" ", "")
        if not username:
            username = full_name.replace(" ", "").lower() or "candidate"
        base = username
        i = 1
        while CustomUser.objects.filter(username=username).exists():
            username = f"{base}_{i}"
            i += 1
        user=CustomUser.objects.create_user(
            username=username,
            full_name=full_name,
            phone_number=phone_number,
            email=request.POST.get("email", "").strip(),
            city=request.POST.get("city", "").strip(),
            gender=request.POST.get("gender"),
            format=request.POST.get("format"),
            level=request.POST.get("level"),
            languages=(request.POST.get("languages") or "PYTHON"),
            englishlevel=request.POST.get("englishlevel") or "Не указан",
            years_experience=int(request.POST.get("years_experience") or 0),
            resume_url=request.POST.get("resume_url", "").strip(),
            about=request.POST.get("about", "").strip(),
            consent=True if request.POST.get("consent") else False,
            password=None,
        )
        group, _ = Group.objects.get_or_create(name="Кандидаты")
        user.groups.add(group)
        user.save()
        
        return redirect("success")

    return render(request, "users/apply.html")


def admin_login_view(request):
    if request.method == "POST":
        form = CaptchaAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("applications")
    else:
        form = CaptchaAuthenticationForm(request)

    return render(request, "users/login.html", {"form": form})

def admin_logout_view(request):
    logout(request)
    return redirect("login")

def applications_list_view(request):
    applications = CustomUser.objects.all().order_by("-created_at")
    return render(
        request,
        "users/applications_list.html",
        {"applications": applications}
    )
def success_view(request):
    return render(request, "users/success.html")
