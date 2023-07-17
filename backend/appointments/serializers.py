from rest_framework import serializers
from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Appointment
        field = ['id', 'user', 'reason', 'appt_date', 'start', 'end', 'vet_name']
        depth = 1

