# Generated by Django 4.2 on 2024-04-30 20:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("buzopolis_tienda", "0002_colorproducto_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="producto",
            name="created",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
