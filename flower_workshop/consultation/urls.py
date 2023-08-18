from .views import consultation, ConsultationFormView

from django.urls import path

app_name = "consultation"

urlpatterns = [
    path('', consultation, name='consultation'),
    path('summit/', ConsultationFormView.as_view(), name="submit_form"),
]
