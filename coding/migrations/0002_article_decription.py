# Generated by Django 3.2.5 on 2022-02-13 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='decription',
            field=models.TextField(null=True),
        ),
    ]
