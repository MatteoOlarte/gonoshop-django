from decimal import Decimal
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required

from gonoshop_tienda.models import Producto
from .forms import FormularioPagos


# Create your views here.
@login_required
def pago_producto(request: HttpRequest, id: int) -> HttpResponse:
    producto = get_object_or_404(Producto, id=id)
    form = FormularioPagos()
    success = False

    producto.precio = producto.precio * Decimal(1.19)
    print(request.method)

    if request.method == 'POST':        
        form = FormularioPagos(request.POST)
        print(form.data)

        if form.is_valid():
            success = True
            cd = form.cleaned_data
            print(cd['email'])

    context = {
        'producto': producto,
        'form': form,
        'success': success
    }
    return render(request, 'gonoshop_pagos/pago_producto/template.html', context)