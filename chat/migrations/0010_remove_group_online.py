# Generated by Django 4.2.3 on 2023-07-26 10:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0009_alter_group_options_alter_group_group_pic"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="group",
            name="online",
        ),
    ]