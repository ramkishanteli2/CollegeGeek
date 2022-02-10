# Generated by Django 3.2.7 on 2021-09-30 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0009_student_currentsem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('filefield', models.FileField(upload_to='material')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.subject')),
            ],
        ),
    ]
