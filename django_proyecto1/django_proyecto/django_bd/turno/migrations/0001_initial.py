# Generated by Django 4.2.4 on 2023-10-24 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dni', models.CharField(max_length=10)),
                ('Especialidad', models.CharField(max_length=50)),
                ('Fecha', models.DateField()),
                ('Hora', models.TimeField()),
            ],
        ),
    ]
