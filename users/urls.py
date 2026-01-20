from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path("apply/",views.CandidateApplyView.as_view(), name="apply"),
    path("success/", views.success_view, name="success"),

    path("login/", views.AdminLoginView.as_view(), name="login"),
    path("logout/", views.AdminLogoutView.as_view(), name="logout"),

    path("applications/", views.ApplicationListView.as_view(), name="applications"),
]
