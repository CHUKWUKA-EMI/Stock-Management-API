# Generated by Django 3.0.8 on 2020-07-15 20:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('stockApp', '0004_auto_20200715_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
