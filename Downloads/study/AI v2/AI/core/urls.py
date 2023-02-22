from django.urls import path
from core import views

urlpatterns = [
    path("", views.generate_text,name='generate_text')]