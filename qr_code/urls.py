from django.urls import path
from .views import qr_home


urlpatterns = [
    path("", qr_home)
]


