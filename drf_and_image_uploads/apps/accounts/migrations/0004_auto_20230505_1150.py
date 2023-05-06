# Generated by Django 3.1.8 on 2023-05-05 11:50

from django.db import migrations, models
import drf_and_image_uploads.apps.accounts.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20230505_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.FileField(blank=True, upload_to=drf_and_image_uploads.apps.accounts.models.upload_to, verbose_name='resume'),
        ),
    ]