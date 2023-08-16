from django.shortcuts import render


def catalog(request):
    return render(request, 'bouquets/catalog.html', context={}) 


def card(request, pk): 
    return render(request, 'bouquets/card.html', context={})


def result(request): 
    return render(request, 'bouquets/result.html', context={})


def quiz(request):
    return render(request, 'bouquets/quiz.html')


def quiz_step(request):
    return render(request, 'bouquets/quiz-step.html')
