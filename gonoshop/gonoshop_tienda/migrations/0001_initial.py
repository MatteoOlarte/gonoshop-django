# Generated by Django 4.2 on 2024-05-04 02:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ColorProducto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre",
                    models.CharField(max_length=250, verbose_name="Nombre Color"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Personalizado",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="TipoProducto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre",
                    models.CharField(max_length=250, verbose_name="Nombre Categoría"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Producto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=250)),
                ("slug", models.SlugField(max_length=250)),
                ("description", models.TextField(max_length=2500)),
                ("imagen", models.ImageField(upload_to="tienda/productos/%Y/%m/%d/%H")),
                (
                    "talla",
                    models.CharField(
                        choices=[
                            ("xs", "extra small"),
                            ("s", "small"),
                            ("m", "medium"),
                            ("l", "large"),
                            ("xl", "extra large"),
                            ("xxl", "extra extra large"),
                        ],
                        default="s",
                        max_length=3,
                    ),
                ),
                ("precio", models.DecimalField(decimal_places=2, max_digits=20)),
                ("stock", models.IntegerField()),
                ("disponibilidad", models.BooleanField(default=True, editable=False)),
                ("publicado", models.BooleanField(default=False)),
                ("created", models.DateField(auto_now_add=True)),
                (
                    "color",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="+",
                        to="gonoshop_tienda.colorproducto",
                    ),
                ),
                (
                    "tipo_producto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="productos",
                        related_query_name="producto",
                        to="gonoshop_tienda.tipoproducto",
                    ),
                ),
            ],
            options={
                "verbose_name": "producto",
                "verbose_name_plural": "productos",
                "ordering": ["-precio"],
            },
        ),
        migrations.CreateModel(
            name="ComentarioProducto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=250)),
                ("contenido", models.CharField(max_length=25000)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comentarios",
                        related_query_name="comentario",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "producto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comentarios",
                        related_query_name="comentario",
                        to="gonoshop_tienda.producto",
                    ),
                ),
            ],
        ),
        migrations.AddIndex(
            model_name="producto",
            index=models.Index(fields=["slug"], name="idx_producto_slug"),
        ),
        migrations.AddIndex(
            model_name="producto",
            index=models.Index(fields=["-precio"], name="idx_producto_precio"),
        ),
    ]