# Generated by Django 2.2.3 on 2020-04-11 00:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=75, unique=True)),
                ('comment_text', models.TextField(blank=True, max_length=120, null=True)),
                ('date_added', models.DateTimeField(default=datetime.datetime(2020, 4, 11, 0, 5, 16, 70659), verbose_name='Date added')),
                ('owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]