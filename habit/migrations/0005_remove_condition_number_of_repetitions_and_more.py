# Generated by Django 5.1.3 on 2024-11-17 12:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habit", "0004_alter_habit_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="condition",
            name="number_of_repetitions",
        ),
        migrations.AlterField(
            model_name="condition",
            name="frequency",
            field=models.PositiveSmallIntegerField(
                default=1,
                max_length=20,
                validators=[
                    django.core.validators.MaxValueValidator(7),
                    django.core.validators.MinValueValidator(1),
                ],
                verbose_name="Периодичность выполнения в днях",
            ),
        ),
    ]
