# Generated by Django 3.2.7 on 2021-09-21 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Livraria', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Usuário',
            new_name='Usuario',
        ),
    ]
