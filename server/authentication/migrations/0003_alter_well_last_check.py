# Generated by Django 4.1.7 on 2023-03-12 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_well_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='well',
            name='last_check',
            field=models.DateTimeField(blank=True),
        ),
    ]
