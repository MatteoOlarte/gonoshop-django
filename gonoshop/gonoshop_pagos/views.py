from django.conf import settings
from decimal import Decimal
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage

from gonoshop_tienda.models import Producto
from .forms import FormularioPagos


# Create your views here.
@login_required
def pago_producto(request: HttpRequest, id: int) -> HttpResponse:
    producto = get_object_or_404(Producto, id=id)
    form = FormularioPagos()
    success = False
    producto.precio = producto.precio * Decimal(1.19)
 
    if request.method == 'POST':        
        form = FormularioPagos(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            name = cd['nombre']
            email = cd['email']
            direcion = cd['direcion']
            success = True

            message = EmailMessage(
                'Compras Gonoshop', 
                f'Se ha registrado una nueva compra de los productos de la tienda, producto comprado: {request.build_absolute_uri(producto.get_absolute_url())}, nombre del comprador: {name}, direcion de envió: {direcion}, numero de aprobación #9112001',
                reply_to=[email], to=[settings.EMAIL_HOST_USER])
            message.send()



    context = {
        'producto': producto,
        'form': form,
        'success': success
    }
    return render(request, 'gonoshop_pagos/pago_producto/template.html', context)