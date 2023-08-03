# serializers.py
from rest_framework import serializers
from .models import Patient, User


class PatientSerializer(serializers.ModelSerializer):
    # Add fields for the user's first name and last name
    user_first_name = serializers.ReadOnlyField(source='user.first_name')
    user_last_name = serializers.ReadOnlyField(source='user.last_name')

    class Meta:
        model = Patient
        fields = ['id', 'user_first_name', 'user_last_name', 'address', 'treatment_type', 'cholesterol_level', 'weight_lb', 'bp_1s', 'notes', 'status', 'assignedDoctorId', 'last_updated', 'updated_by']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
