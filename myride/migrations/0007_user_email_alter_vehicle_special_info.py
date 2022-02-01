# Generated by Django 4.0.1 on 2022-01-31 18:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myride', '0006_remove_ride_arrival_timestamp_ride_arrival_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254, verbose_name='email address'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='special_info',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]