from django.urls import path
from .views import HomeView, PersonalView

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("sobre-mi/", PersonalView.as_view(), name="personal"),
]




