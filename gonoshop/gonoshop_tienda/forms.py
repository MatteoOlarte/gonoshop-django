from django import forms

from .models import ColorProducto as Color
from .models import TipoProducto as Categoria


# Create forms views here.
class FiltroProductos(forms.Form):
    nombre = forms.CharField(required=False)
    precio_min = forms.DecimalField(required=False)
    precio_max = forms.DecimalField(required=False)
    color = forms.ChoiceField(required=False)
    categoria = forms.ChoiceField(required=False)

    def __init__(self, colors_list: list[Color], categories_list: list[Categoria], *args, **kwargs) -> None:
        super(FiltroProductos, self).__init__(*args, **kwargs)
        color_choices = list(map(lambda data: (data.id, data.nombre.upper()), colors_list))
        color_choices.append((None, 'ALL'))
        color_choices.sort(key=lambda it: it[1])
        category_choices = list(map(lambda data: (data.id, data.nombre.upper()), categories_list))
        category_choices.append((None, 'ALL'))
        category_choices.sort(key=lambda it: it[1])

        self.fields['nombre'].widget.attrs['placeholder'] = 'Adidas Essentials'
        self.fields['nombre'].widget.attrs['class'] = 'form-control'

        self.fields['precio_min'].widget.attrs['placeholder'] = f'{0:,.2f}'
        self.fields['precio_min'].widget.attrs['class'] = 'form-control'

        self.fields['precio_max'].widget.attrs['placeholder'] = f'{999999:,.2f}'
        self.fields['precio_max'].widget.attrs['class'] = 'form-control'

        self.fields['color'].choices = color_choices
        self.fields['color'].widget.attrs['class'] = 'form-select'

        self.fields['categoria'].choices = category_choices
        self.fields['categoria'].widget.attrs['class'] = 'form-select'