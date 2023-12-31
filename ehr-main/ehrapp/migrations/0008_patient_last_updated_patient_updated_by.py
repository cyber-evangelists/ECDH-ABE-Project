# Generated by Django 4.2.3 on 2023-07-22 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ehrapp", "0007_remove_patient_bp_1d_remove_patient_bp_2d_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="last_updated",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="patient",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="updated_patients",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
