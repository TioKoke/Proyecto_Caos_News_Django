# Generated by Django 4.0.4 on 2022-05-12 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('nombre', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('nombre', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=60)),
                ('correo', models.CharField(max_length=60)),
            ],
        ),
    ]