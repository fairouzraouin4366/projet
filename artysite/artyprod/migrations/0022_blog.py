# Generated by Django 4.2.1 on 2023-05-23 21:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artyprod', '0021_remove_demandeprojet_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('datedep', models.DateField(default=datetime.date.today, null=True)),
                ('source', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
