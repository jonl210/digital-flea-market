# Generated by Django 4.1.5 on 2023-02-01 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_alter_itemsupplier_valuesuppliedtodate"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customer",
            old_name="ChardNum",
            new_name="CardNum",
        ),
    ]