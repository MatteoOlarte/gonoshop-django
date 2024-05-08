import re
from typing import Self
from django import forms
from django.forms import ValidationError


# Create your forms here.
class FormularioPagos(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    direcion = forms.CharField()
    numero_tarjeta = forms.CharField()
    cvv = forms.CharField()
    fecha_vencimiento = forms.DateField()

    def __init__(self: Self, *args, **kwargs) -> None:
        super(FormularioPagos, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['direcion'].widget.attrs['class'] = 'form-control'
        self.fields['numero_tarjeta'].widget.attrs['class'] = 'form-control'
        self.fields['cvv'].widget.attrs['class'] = 'form-control'
        self.fields['fecha_vencimiento'].widget.attrs['class'] = 'form-control'
        
    def clean_numero_tarjeta(self: Self):
        cd: dict = self.cleaned_data

        if re.fullmatch(r'^[1-9][0-9]{13,18}$', cd.get('numero_tarjeta')):
            return cd['numero_tarjeta']
        
        raise ValidationError('El número de tarjeta ingresado es inválido. Por favor, verifica la información y vuelve a intentarlo')#cuando el numero de tarjeta sea invalido

    def clean_cvv(self: Self):
        cd: dict = self.cleaned_data

        if re.fullmatch(r'^[1-9][0-9]{2}$', cd.get('cvv')):
            return cd['cvv']
        
        raise ValidationError('El código CVV ingresado es inválido. Por favor, verifica y asegúrate de que el CVV sea correcto')#cuando el cvv del la tarjeta sea invalido
