# Generated by Django 4.2.4 on 2023-08-26 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_filmes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filme',
            old_name='titulo',
            new_name='nome',
        ),
    ]
