# Generated by Django 5.0.1 on 2024-03-13 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("prototype", "0002_alter_richtext_content"),
    ]

    operations = [
        migrations.AddField(
            model_name="location",
            name="children_tag",
            field=models.CharField(
                choices=[("ul", "list item"), ("div class='row'", "row"), ("div class='col'", "column")],
                default="ul",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="location",
            name="node_tag",
            field=models.CharField(
                choices=[
                    ("li", "list item"),
                    ("div class='row'", "row"),
                    ("div class='col'", "column"),
                    ("h1", "1 - heading"),
                    ("h3", "3 - heading"),
                    ("h5", "5 - heading"),
                ],
                default="li",
                max_length=20,
            ),
        ),
    ]
