from django.urls import path
from p_library.views import index

urlpatterns = [
    path('index', index),
]
