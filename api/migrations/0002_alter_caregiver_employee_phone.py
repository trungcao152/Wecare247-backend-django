# Generated by Django 4.1.5 on 2023-03-13 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caregiver',
            name='employee_phone',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
