# Generated by Django 5.0.5 on 2024-05-09 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0019_alter_studentresult_ue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentresult',
            name='ue',
        ),
    ]