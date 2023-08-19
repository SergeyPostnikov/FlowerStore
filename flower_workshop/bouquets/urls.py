from django.urls import path

from .views import card
from .views import catalog
from .views import quiz
from .views import quiz_step
from .views import result

app_name = 'bouquets'

urlpatterns = [
    path('catalog/', catalog, name='catalog'),
    path('result/', result, name='result'),
    path('quiz/', quiz, name='quiz'),
    path('quiz-step/', quiz_step, name='quiz-step'),
    path('card/<int:pk>/', card, name='card'),
]
