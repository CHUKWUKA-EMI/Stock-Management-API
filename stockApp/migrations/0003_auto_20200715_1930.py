# Generated by Django 3.0.8 on 2020-07-15 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockApp', '0002_auto_20200715_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='id',
            field=models.UUIDField(blank=True, primary_key=True, serialize=False),
        ),
    ]
