# Generated by Django 4.1.2 on 2022-11-03 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cadastros', '0002_alter_professor_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='Senha',
        ),
    ]