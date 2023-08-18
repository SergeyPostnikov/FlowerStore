from django.core.exceptions import ValidationError
from django.forms import ModelForm
from phonenumber_field.formfields import PhoneNumberField

from consultation.models import Consultation


class CounsultationForm(ModelForm):
    phone = PhoneNumberField()
    phone.error_messages['invalid'] = "Введите корректный номер телефона, например: +7 (933) 933-33-33"
    class Meta:
        model = Consultation
        fields = ["name", "phone"]
