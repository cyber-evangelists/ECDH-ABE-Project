from django.dispatch import receiver
from ehrapp.signals import doctor_details_edited
from ehrapp.models import Patient, Doctor

@receiver(doctor_details_edited)
def notify_patient_on_doctor_edit(sender, instance, **kwargs):
    # Extract necessary information from the instance and perform notification logic
    doctor = instance
    patient = Patient.objects.get(doctor=doctor)  # You need to define this relationship in your models
    
    # Implement your notification logic here, such as sending an email or a notification to the patient
