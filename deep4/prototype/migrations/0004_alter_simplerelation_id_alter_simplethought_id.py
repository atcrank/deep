# Generated by Django 4.2.4 on 2023-12-23 01:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("prototype", "0003_alter_simplerelation_id_alter_simplethought_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="simplerelation",
            name="id",
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="simplethought",
            name="id",
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
