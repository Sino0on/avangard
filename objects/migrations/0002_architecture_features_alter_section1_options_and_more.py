# Generated by Django 5.1.3 on 2024-12-07 12:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("objects", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Architecture",
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
                ("title", models.CharField(max_length=123)),
            ],
        ),
        migrations.CreateModel(
            name="Features",
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
                ("title", models.CharField(max_length=123)),
                ("mini_description", models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name="section1",
            options={"verbose_name": "О комплексе"},
        ),
        migrations.AlterModelOptions(
            name="section2",
            options={"verbose_name": "В цифрах"},
        ),
        migrations.AlterModelOptions(
            name="section3",
            options={"verbose_name": "День и Ночь"},
        ),
        migrations.AlterModelOptions(
            name="section4",
            options={"verbose_name": "Планы этажей"},
        ),
        migrations.AlterModelOptions(
            name="section5",
            options={"verbose_name": "Подземная парковка"},
        ),
        migrations.AlterModelOptions(
            name="section6",
            options={"verbose_name": "Архитектура"},
        ),
        migrations.AlterModelOptions(
            name="section7",
            options={"verbose_name": "Галерея"},
        ),
        migrations.AlterModelOptions(
            name="section8",
            options={"verbose_name": "Преимущества"},
        ),
        migrations.AlterModelOptions(
            name="section9",
            options={"verbose_name": "Интересное рядом"},
        ),
        migrations.RemoveField(
            model_name="section4",
            name="under_parking_layout",
        ),
        migrations.RemoveField(
            model_name="section5",
            name="images",
        ),
        migrations.RemoveField(
            model_name="section6",
            name="advantages",
        ),
        migrations.RemoveField(
            model_name="section7",
            name="interest_nearby",
        ),
        migrations.RemoveField(
            model_name="section8",
            name="location_description",
        ),
        migrations.RemoveField(
            model_name="section8",
            name="location_image_first",
        ),
        migrations.RemoveField(
            model_name="section8",
            name="location_image_second",
        ),
        migrations.RemoveField(
            model_name="section9",
            name="etaps_url",
        ),
        migrations.RemoveField(
            model_name="section9",
            name="live_url",
        ),
        migrations.RemoveField(
            model_name="section9",
            name="youtube_url",
        ),
        migrations.AddField(
            model_name="section4",
            name="floorschemas",
            field=models.ManyToManyField(to="objects.floorschema"),
        ),
        migrations.AddField(
            model_name="section5",
            name="under_parking_layout",
            field=models.ImageField(default=1, upload_to="images/buildings/"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="section7",
            name="images",
            field=models.ManyToManyField(to="objects.imagegallery"),
        ),
        migrations.AddField(
            model_name="section8",
            name="advantages",
            field=models.ManyToManyField(to="objects.advantage"),
        ),
        migrations.AddField(
            model_name="section9",
            name="interest_nearby",
            field=models.ManyToManyField(to="objects.interestingnearbybuilding"),
        ),
        migrations.AlterField(
            model_name="section7",
            name="building",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="section_67",
                to="objects.building",
            ),
        ),
        migrations.AddField(
            model_name="section6",
            name="architecture",
            field=models.ManyToManyField(to="objects.architecture"),
        ),
        migrations.AddField(
            model_name="architecture",
            name="features",
            field=models.ManyToManyField(to="objects.features"),
        ),
        migrations.CreateModel(
            name="Section10",
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
                ("location_description", models.TextField()),
                (
                    "location_image_first",
                    models.ImageField(upload_to="images/buildings/"),
                ),
                (
                    "location_image_second",
                    models.ImageField(upload_to="images/buildings/"),
                ),
                (
                    "building",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="section_10",
                        to="objects.building",
                    ),
                ),
            ],
            options={
                "verbose_name": "Локация",
            },
        ),
        migrations.CreateModel(
            name="Section11",
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
                ("youtube_url", models.URLField()),
                ("live_url", models.URLField()),
                ("etaps_url", models.URLField()),
                (
                    "building",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="section_11",
                        to="objects.building",
                    ),
                ),
            ],
            options={
                "verbose_name": "Футер",
            },
        ),
    ]
