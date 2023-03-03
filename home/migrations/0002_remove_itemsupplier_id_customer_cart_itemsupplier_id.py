# Generated by Django 4.1.5 on 2023-02-24 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="itemsupplier",
            name="id",
        ),
        migrations.AddField(
            model_name="customer",
            name="cart",
            field=models.ManyToManyField(default=None, to="home.items"),
        ),
        migrations.AddField(
            model_name="itemsupplier",
            name="ID",
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
