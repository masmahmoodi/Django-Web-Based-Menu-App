# Generated by Django 4.2.6 on 2023-12-17 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_item_item_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='user_name',
        ),
    ]
