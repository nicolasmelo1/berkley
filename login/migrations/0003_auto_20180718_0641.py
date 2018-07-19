# Generated by Django 2.0.7 on 2018-07-18 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20180718_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextended',
            name='company',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='login.Companies'),
        ),
        migrations.AlterField(
            model_name='userextended',
            name='profile',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='login.Profiles'),
        ),
    ]
