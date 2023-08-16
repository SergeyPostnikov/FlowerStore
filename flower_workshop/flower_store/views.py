from django.shortcuts import render


def catalog(request):
    return render(request, 'catalog.html', context={}) #bouq


def consultation(request):
    return render(request, 'consultation.html', context={}) #advize


def card(request, pk): #bouqett
    return render(request, 'card.html', context={})


def result(request): #bouqett
    return render(request, 'result.html', context={})


def quiz(request):#bouqett
    return render(request, 'quiz.html')


def quiz_step(request):#bouqett
    return render(request, 'quiz-step.html')
