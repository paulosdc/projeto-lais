# Generated by Django 4.1.2 on 2022-11-03 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cadastros', '0003_remove_professor_senha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='DataNascimento',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='Nome',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='Titulacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Cadastros.titulacao'),
        ),
    ]
