# Generated by Django 4.1.7 on 2023-03-12 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GazpromUser',
            fields=[
                ('login', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('surname', models.CharField(blank=True, max_length=255)),
                ('isAdmin', models.BooleanField(default=False)),
                ('isDeveloper', models.BooleanField(default=False)),
                ('isLogin', models.BooleanField(default=False)),
                ('joined_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('token', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Well',
            fields=[
                ('created_at', models.DateTimeField(auto_created=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('conditions', models.CharField(max_length=255, null=True)),
                ('geo', models.CharField(max_length=255, null=True)),
                ('status', models.IntegerField(null=True)),
                ('last_check', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('well_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authentication.well')),
            ],
        ),
    ]
