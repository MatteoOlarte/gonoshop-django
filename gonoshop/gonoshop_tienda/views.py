from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import FiltroProductos
from .models import ColorProducto
from .models import Producto
from .models import TipoProducto
from .models import SacoPersonalizado
from django.shortcuts import render, redirect
from .forms import SacoPersonalizadoForm

# Create your views here.   
def lista_productos_all(request: HttpRequest) -> HttpResponse:
    colores = list(ColorProducto.objects.all())
    tipos = list(TipoProducto.objects.all())
    productos: Producto = None
    form: ColorProducto = None

    if request.method == 'POST':
        form = FiltroProductos(colores, tipos, request.POST)

        if form.is_valid():
            cd: dict = form.cleaned_data
            nombre = cd['nombre']
            precio_min = cd.get('precio_min') or 1
            precio_max = cd.get('precio_max') or 999_999_999
            color = cd['color']
            categoria = cd['categoria']

            productos = Producto.objects.filter(
                Q(nombre__icontains=nombre) | Q(description__icontains=nombre),
                precio__gt=precio_min,
                precio__lt=precio_max
            )
            if color:
                productos = productos.filter(color__id__in=[color])
            if categoria:
                productos = productos.filter(tipo_producto__id__in=[categoria])
    else:
        productos = Producto.objects.all()
        form = FiltroProductos(colores, tipos)

    context = {
        'url_name': 'tienda',
        'productos': productos,
        'form': form
    }
    return render(request, 'gonoshop_tienda/lista_productos/template.html', context)


def detalle_producto(request: HttpRequest, nombre_producto: str, _id: int) -> HttpResponse:
    producto = get_object_or_404(Producto, id=_id)
    context = {
        'url_name': 'tienda',
        'producto': producto
    }
    return render(request, 'gonoshop_tienda/detalle_producto/template.html', context)


def editor_producto(request):
    if request.method == 'POST':
        form = SacoPersonalizadoForm(request.POST, request.FILES)
        if form.is_valid():
            saco_personalizado = form.save()
            # Lógica para agregar el saco personalizado al carrito de compras
            return redirect('pagina_de_carrito')  # Redirigir a la página de carrito de compras
    else:
        form = SacoPersonalizadoForm()
    return render(request, 'gonoshop_tienda/editor_producto/template.html', {'form': form})