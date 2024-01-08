# Generated by Django 4.2.3 on 2023-07-29 16:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0012_alter_group_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="chatmessages",
            name="file",
            field=models.FileField(
                blank=True, max_length=655, null=True, upload_to="chats/file/"
            ),
        ),
        migrations.AddField(
            model_name="chatmessages",
            name="message_type",
            field=models.CharField(
                choices=[
                    ("text", "Text"),
                    ("link", "Link"),
                    ("pic", "Picture"),
                    ("file", "File"),
                ],
                default="text",
                max_length=255,
            ),
        ),
    ]
