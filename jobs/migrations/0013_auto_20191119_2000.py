# Generated by Django 2.2.1 on 2019-11-19 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0012_job_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='order',
            field=models.PositiveIntegerField(),
        ),
    ]
