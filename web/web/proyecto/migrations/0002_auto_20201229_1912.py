# Generated by Django 3.1.4 on 2020-12-30 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ejemplomedicion',
            old_name='valor',
            new_name='valor1',
        ),
        migrations.AddField(
            model_name='ejemplomedicion',
            name='valor2',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='ejemplomedicion',
            name='valor3',
            field=models.FloatField(default=0),
        ),
    ]