# Generated by Django 4.1.4 on 2022-12-21 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0006_alter_livros_data_cadastro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='data_cadastro',
            field=models.DateTimeField(),
        ),
    ]
