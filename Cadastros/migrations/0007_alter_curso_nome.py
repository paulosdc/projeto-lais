# Generated by Django 4.1.2 on 2022-11-03 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cadastros', '0006_alter_professor_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='Nome',
            field=models.CharField(max_length=120),
        ),
    ]
