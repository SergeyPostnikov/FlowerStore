from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Bouquet


def catalog(request):
    bouquets = Bouquet.objects.all()
    paginator = Paginator(bouquets, 3)
    page_obj = paginator.get_page(request.GET.get("page", 1))
    if request.htmx:
        return render(request, 'bouquets/components/catalog_page.html', context={'page_obj': page_obj})
    return render(request, 'bouquets/catalog.html', context={'page_obj': page_obj})


def card(request, pk):
    return render(request, 'bouquets/card.html', context={'bouquet': get_object_or_404(Bouquet, pk=pk)})


def result(request):
    return render(request, 'bouquets/result.html', context={})


def quiz(request):
    return render(request, 'bouquets/quiz.html')


def quiz_step(request):
    return render(request, 'bouquets/quiz-step.html')
