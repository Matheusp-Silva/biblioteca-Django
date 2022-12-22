# Generated by Django 4.1.4 on 2022-12-21 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=30)),
                ('co_autor', models.CharField(max_length=30)),
                ('data_cadastro', models.DateTimeField()),
                ('emprestado', models.BooleanField(default=False)),
                ('nome_emprestado', models.CharField(max_length=30)),
                ('data_emprestado', models.DateTimeField()),
                ('data_devolucao', models.DateTimeField()),
                ('tempo_duracao', models.DateTimeField()),
            ],
        ),
    ]
