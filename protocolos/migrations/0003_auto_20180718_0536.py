# Generated by Django 2.0.7 on 2018-07-18 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protocolos', '0002_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protocols',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='protocols',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]