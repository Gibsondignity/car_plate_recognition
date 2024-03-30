# Generated by Django 4.1.7 on 2023-02-23 12:07

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_acount_user_second_name_alter_acount_user_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acount_user',
            name='profile',
            field=models.FileField(blank=True, null=True, upload_to='profile/', validators=[account.models.validate_image]),
        ),
    ]
