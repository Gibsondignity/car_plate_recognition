# Generated by Django 4.2.11 on 2024-04-21 11:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apm_app', '0008_carowner_remove_carinfo_owner_name_entrycars_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carinfo',
            name='car_owner',
        ),
        migrations.AddField(
            model_name='carinfo',
            name='owner_address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='carinfo',
            name='owner_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='carinfo',
            name='owner_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='carinfo',
            name='owner_national_id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='carinfo',
            name='owner_nationality',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='carinfo',
            name='owner_phone',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='car_model',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='car_number',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='car_type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='color',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='date_of_reg',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 21, 11, 50, 11, 316800, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='owner_dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.DeleteModel(
            name='CarOwner',
        ),
    ]