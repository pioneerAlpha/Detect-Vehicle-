# from django.urls import path
# from .views import IndexView
from django.urls import path

from . import views

urlpatterns = [
	path("", views.index, name="index"),
]