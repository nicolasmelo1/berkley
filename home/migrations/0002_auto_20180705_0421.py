# Generated by Django 2.0.7 on 2018-07-05 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historico',
            old_name='protocolo_id',
            new_name='protocolo',
        ),
        migrations.AddField(
            model_name='historico',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historico',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
