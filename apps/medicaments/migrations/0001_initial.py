# Generated by Django 5.0.6 on 2024-07-07 21:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Medicaments",
            fields=[
                ("Medicament_id", models.AutoField(primary_key=True, serialize=False)),
                ("medicament", models.CharField(max_length=50)),
                ("for_what", models.TextField()),
                ("type", models.CharField(max_length=50)),
                ("costs", models.DecimalField(decimal_places=2, max_digits=10)),
                ("dose", models.IntegerField()),
                ("when_to_use", models.CharField(max_length=30)),
                (
                    "patient_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "medicaments",
            },
        ),
    ]
