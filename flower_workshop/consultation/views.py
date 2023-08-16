from django.shortcuts import render


def consultation(request):
    return render(request, 'consultation/consultation.html', context={})
