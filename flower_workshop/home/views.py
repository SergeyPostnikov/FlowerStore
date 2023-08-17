from django.shortcuts import render

from bouquets.models import Bouquet


def index(request):
    return render(
        request,
        'home/index.html',
        context={
            'recommended_bouquets': Bouquet.objects.filter(recommended=True),
        },
    )
