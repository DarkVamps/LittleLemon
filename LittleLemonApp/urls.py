from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = "LittleLemonApp"
urlpatterns = [
    path("api-token-auth/", obtain_auth_token),
    path("form/", views.form_view),
]
