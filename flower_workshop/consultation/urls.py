from .views import consultation

from django.urls import path

urlpatterns = [
    path('', consultation, name='consultation')
]
