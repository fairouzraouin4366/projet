# Generated by Django 4.2.1 on 2023-05-23 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artyprod', '0017_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demandeprojet',
            name='equipe',
        ),
        migrations.RemoveField(
            model_name='demandeprojet',
            name='service',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='DemandeProjet',
        ),
    ]
