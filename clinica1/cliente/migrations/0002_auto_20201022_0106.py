# Generated by Django 3.1.2 on 2020-10-22 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Horario_disponivel',
            new_name='HorarioDisponivel',
        ),
        migrations.AddField(
            model_name='clientes',
            name='horario_disponivel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.horariodisponivel'),
        ),
    ]
