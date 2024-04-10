# Generated by Django 5.0.4 on 2024-04-10 13:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estudiantes', to='estudiante.curso'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='nota_curso',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]