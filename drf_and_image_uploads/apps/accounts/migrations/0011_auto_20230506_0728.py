# Generated by Django 3.1.8 on 2023-05-06 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20230506_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contact',
            field=models.CharField(default='777', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='id_number',
            field=models.CharField(default='777', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='middle_name',
            field=models.CharField(default='777', max_length=150),
        ),
    ]
