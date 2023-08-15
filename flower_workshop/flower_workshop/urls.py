"""
URL configuration for flower_workshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from flower_store.views import catalog
from flower_store.views import index
from flower_store.views import order
from flower_store.views import order_step
from flower_store.views import quiz
from flower_store.views import quiz_step
from flower_store.views import result

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('catalog/', catalog, name='catalog'),
    path('order/', order, name='order'),
    path('order-step/', order_step, name='order-step'),
    path('result/', result, name='result'),
    path('quiz/', quiz, name='quiz'),
    path('quiz-step/', quiz_step, name='quiz-step'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
