
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .models import CustomUser
from .forms import CaptchaAuthenticationForm
from django.contrib.auth.models import Group
from django.views import generic

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy


class CandidateApplyView(generic.CreateView):
    model = CustomUser
    template_name = "users/apply.html"
    fields = [
        "full_name",
        "phone_number",
        "email",
        "city",
        "gender",
        "format",
        "level",
        "languages",
        "englishlevel",
        "years_experience",
        "resume_url",
        "about",
    ]
    success_url = "/success/"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.username = user.phone_number or user.full_name
        user.set_unusable_password()
        user.save()
        group, _ = Group.objects.get_or_create(name="Кандидаты")
        user.groups.add(group)
        return redirect(self.success_url)    
    
    def form_invalid(self, form):
     print("FORM ERRORS:", form.errors)
     return super().form_invalid(form)

# def candidate_apply_view(request):
    # if request.method == "POST":
    #     full_name = request.POST.get("full_name", "").strip()
    #     phone_number = request.POST.get("phone_number", "").strip()
    #     username = phone_number.replace("+", "").replace(" ", "")
    #     if not username:
    #         username = full_name.replace(" ", "").lower() or "candidate"
    #     base = username
    #     i = 1
    #     while CustomUser.objects.filter(username=username).exists():
    #         username = f"{base}_{i}"
    #         i += 1
    #     user=CustomUser.objects.create_user(
    #         username=username,
    #         full_name=full_name,
    #         phone_number=phone_number,
    #         email=request.POST.get("email", "").strip(),
    #         city=request.POST.get("city", "").strip(),
    #         gender=request.POST.get("gender"),
    #         format=request.POST.get("format"),
    #         level=request.POST.get("level"),
    #         languages=(request.POST.get("languages") or "PYTHON"),
    #         englishlevel=request.POST.get("englishlevel") or "Не указан",
    #         years_experience=int(request.POST.get("years_experience") or 0),
    #         resume_url=request.POST.get("resume_url", "").strip(),
    #         about=request.POST.get("about", "").strip(),
    #         consent=True if request.POST.get("consent") else False,
    #         password=None,
    #     )
    #     group, _ = Group.objects.get_or_create(name="Кандидаты")
    #     user.groups.add(group)
    #     user.save()
        
    #     return redirect("success")

    # return render(request, "users/apply.html")

class AdminLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = CaptchaAuthenticationForm
    
    def dispatch(self, request, *args, **kwargs):
        print(">>> AdminLoginView CALLED")
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        print(">>> SUCCESS URL:", reverse("cineboard:movie_list"))
        return reverse("cineboard:movie_list")

# def admin_login_view(request):
#     if request.method == "POST":
#         form = CaptchaAuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             login(request, form.get_user())
#             return redirect("applications")
#     else:
#         form = CaptchaAuthenticationForm(request)

#     return render(request, "users/login.html", {"form": form})
class AdminLogoutView(LogoutView):
    next_page = reverse_lazy('home_page')
# def admin_logout_view(request):
#     logout(request)
#     return redirect("login")
class ApplicationListView(generic.ListView):
    template_name="users/applications_list.html"
    context_object_name="applications"
    model=CustomUser
    
    def get_queryset(self):
        return self.model.objects.all()
# def applications_list_view(request):
#     applications = CustomUser.objects.all().order_by("-created_at")
#     return render(
#         request,
#         "users/applications_list.html",
#         {"applications": applications}
    # )
def success_view(request):
    return render(request, "users/success.html")
