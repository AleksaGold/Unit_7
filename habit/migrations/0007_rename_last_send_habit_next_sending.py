# Generated by Django 5.1.3 on 2024-11-17 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("habit", "0006_habit_last_send"),
    ]

    operations = [
        migrations.RenameField(
            model_name="habit",
            old_name="last_send",
            new_name="next_sending",
        ),
    ]
