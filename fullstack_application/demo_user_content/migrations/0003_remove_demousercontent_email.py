# Generated by Django 3.0.6 on 2020-05-30 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo_user_content', '0002_demousercontent_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demousercontent',
            name='email',
        ),
    ]
