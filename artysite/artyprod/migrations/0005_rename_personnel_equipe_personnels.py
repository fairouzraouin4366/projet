# Generated by Django 4.2.1 on 2023-05-19 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artyprod', '0004_alter_equipe_personnel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipe',
            old_name='personnel',
            new_name='personnels',
        ),
    ]
