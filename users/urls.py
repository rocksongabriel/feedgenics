from django.urls import path

from .views import DashboardView

app_name = "users"
urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
]
