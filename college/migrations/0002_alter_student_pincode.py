# Generated by Django 3.2.7 on 2021-09-28 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='pincode',
            field=models.IntegerField(null=True),
        ),
    ]