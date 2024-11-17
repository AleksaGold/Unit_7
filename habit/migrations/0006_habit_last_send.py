# Generated by Django 5.1.3 on 2024-11-17 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habit", "0005_remove_condition_number_of_repetitions_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="habit",
            name="last_send",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Дата последней отправки"
            ),
        ),
    ]