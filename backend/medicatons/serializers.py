from rest_framework import serializers
from .models import Medication


class MedicationSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Medications
        fields = ['med_name', 'med_dose', 'med_instr']
        depth = 1