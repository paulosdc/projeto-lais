# Generated by Django 4.1.2 on 2022-11-03 23:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cadastros', '0007_alter_curso_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='CargaHoraria',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(3), django.core.validators.MaxValueValidator(350)]),
        ),
    ]
