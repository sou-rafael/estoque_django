# Generated by Django 4.0.3 on 2022-03-22 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.CharField(max_length=400)),
                ('quantidade', models.IntegerField()),
                ('data_cadastro', models.DateTimeField(verbose_name='date')),
            ],
        ),
    ]