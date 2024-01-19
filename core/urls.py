from django.urls import path
from .views import HomeView, PersonalView, TermsOfUseView, PrivacidadView

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("sobre-mi/", PersonalView.as_view(), name="personal"),
    path('terminos-de-uso/', TermsOfUseView.as_view(), name='terms_of_use'),
    path('politica-de-privacidad/', PrivacidadView.as_view(), name='privacy_policy'),
]




