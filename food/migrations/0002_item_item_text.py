# Generated by Django 4.2.6 on 2023-12-17 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_text',
            field=models.CharField(default='MAooo', max_length=200),
        ),
    ]
