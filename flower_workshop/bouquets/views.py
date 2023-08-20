import random
from decimal import Decimal

from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Bouquet, Event

TOTAL_STEPS = 2


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
    event_id = request.GET.get('event_id')
    price_from = Decimal(request.GET.get('price_from', '0'))
    price_to = Decimal(request.GET.get('price_to', '999999'))
    bouquets = Bouquet.objects.filter(price__gte=price_from, price__lte=price_to)
    if event_id and event_id != 'None':
        events = [get_object_or_404(Event, pk=event_id), ]
        bouquets.filter(events__in=events)

    if bouquets:
        context = {
            "bouquet": random.choice(list(bouquets)),
            "title": "Мы подобрали специально для Вас",
        }
    else:
        context = {
            "bouquet": None,
            "title": "К сожалению, по вашему запросу ничего не нашлось",
        }
    return render(request, 'bouquets/result.html', context)


def quiz_delivery(request):
    return render(
        request,
        'bouquets/quiz.html',
        context={
            'step': 1,
            'total_steps': TOTAL_STEPS,
            'events': Event.objects.all(),
        },
    )


def quiz_payment(request):
    return render(
        request,
        'bouquets/quiz-step.html',
        context={
            'step': 2,
            'total_steps': TOTAL_STEPS,
            'event_id': request.GET.get('event_id'),
        },
    )
