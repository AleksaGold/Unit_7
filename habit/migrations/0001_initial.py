# Generated by Django 5.1.3 on 2024-11-08 11:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Condition",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "place",
                    models.CharField(
                        blank=True,
                        max_length=150,
                        null=True,
                        verbose_name="Место выполнения",
                    ),
                ),
                (
                    "start_time",
                    models.TimeField(verbose_name="Время начала выполнения привычки"),
                ),
                (
                    "frequency",
                    models.CharField(
                        choices=[("daily", "ежедневная"), ("weekly", "еженедельная")],
                        default="daily",
                        max_length=20,
                        verbose_name="Периодичность выполнения",
                    ),
                ),
                (
                    "number_of_repetitions",
                    models.PositiveSmallIntegerField(
                        verbose_name="Количество повторений"
                    ),
                ),
                (
                    "minutes_to_complete",
                    models.PositiveSmallIntegerField(
                        verbose_name="Время на выполнение привычки"
                    ),
                ),
            ],
            options={
                "verbose_name": "Условие выполнения привычки",
                "verbose_name_plural": "Условия выполнения привычек",
                "ordering": ("frequency", "start_time"),
            },
        ),
        migrations.CreateModel(
            name="Reward",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=150, verbose_name="Название вознаграждения"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Описание вознаграждения"
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="rewards/previews",
                        verbose_name="Превью (картинка)",
                    ),
                ),
                (
                    "is_public",
                    models.BooleanField(
                        default=False, verbose_name="Публичное вознаграждение"
                    ),
                ),
            ],
            options={
                "verbose_name": "Вознаграждение",
                "verbose_name_plural": "Вознаграждения",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=150, verbose_name="Название полезной привычки"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Описание полезной привычки"
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="habits/previews",
                        verbose_name="Превью (картинка)",
                    ),
                ),
                (
                    "is_pleasant",
                    models.BooleanField(
                        default=False, verbose_name="Приятная привычка"
                    ),
                ),
                (
                    "is_public",
                    models.BooleanField(
                        default=False, verbose_name="Публичная привычка"
                    ),
                ),
                (
                    "associated_habit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="habits",
                        to="habit.habit",
                        verbose_name="Связанная привычка",
                    ),
                ),
                (
                    "condition",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="habits",
                        to="habit.condition",
                        verbose_name="Условия выполнения привычки",
                    ),
                ),
            ],
            options={
                "verbose_name": "Полезная привычка",
                "verbose_name_plural": "Полезные привычки",
                "ordering": ("name",),
            },
        ),
    ]