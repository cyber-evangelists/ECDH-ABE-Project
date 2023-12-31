# Generated by Django 4.2.3 on 2023-07-10 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehrapp', '0003_delete_patientdischargedetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.CharField(choices=[('Endocrinologist', 'Endocrinologist'), ('Cardiologist', 'Cardiologist'), ('Dermatologists', 'Dermatologists'), ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'), ('Allergists/Immunologists', 'Allergists/Immunologists'), ('Anesthesiologists', 'Anesthesiologists'), ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')], default='Cardiologist', max_length=50),
        ),
    ]
