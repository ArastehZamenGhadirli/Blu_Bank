# Generated by Django 5.1.7 on 2025-03-31 20:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Bill",
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
                ("date", models.DateTimeField(auto_created=True)),
                ("bill_number", models.IntegerField(unique=True)),
                ("amount", models.FloatField()),
                (
                    "title",
                    models.CharField(
                        choices=[
                            ("W", "water"),
                            ("C", "cellphone"),
                            ("E", "Electicity"),
                            ("G", "Gas"),
                        ],
                        default="C",
                        max_length=10,
                    ),
                ),
                ("phonenumber", models.CharField(max_length=10)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Account_Bill",
                        to="home.account",
                    ),
                ),
            ],
        ),
    ]
