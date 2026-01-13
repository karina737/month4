from django.urls import path
from .views import (
    candidate_apply_view,
    admin_login_view,
    admin_logout_view,
    applications_list_view,
    success_view,
)

urlpatterns = [
    path("apply/", candidate_apply_view, name="apply"),
    path("success/", success_view, name="success"),

    path("login/", admin_login_view, name="login"),
    path("logout/", admin_logout_view, name="logout"),

    path("applications/", applications_list_view, name="applications"),
]
