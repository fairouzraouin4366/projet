# Generated by Django 4.2.1 on 2023-05-20 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artyprod', '0012_alter_personnel_photoprs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personnel',
            old_name='fichier_linkedln',
            new_name='linkedln',
        ),
    ]
