# Generated by Django 3.2.12 on 2022-03-25 13:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('advancehomecareapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]