# Generated by Django 3.2.19 on 2023-05-12 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HR_ANALYTICS', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='full_name',
            new_name='username',
        ),
    ]
