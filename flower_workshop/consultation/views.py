from django.shortcuts import render
from django.views import View

from .forms import CounsultationForm
from django.http import Http404

def consultation(request):
    return render(request, 'consultation/consultation.html', context={})


class ConsultationFormView(View):
    def get(self):
        raise Http404
    def post(self, request):
        if request.htmx:
            form = CounsultationForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'consultation/components/consultation_form_success.html', context={'form': form})
            return render(request, 'consultation/components/consultation_form.html', context={'form': form})
        raise Http404