from rest_framework import serializers
from .models import *

class CaregiverSerializer(serializers.ModelSerializer):
    #Adding choices for skill_level from level 1 to 3
    SKILL_LEVELS = [
        ('1', 'Level 1'),
        ('2', 'Level 2'),
        ('3', 'Level 3'),
    ]
    skill_level = serializers.ChoiceField(choices = SKILL_LEVELS)

    class Meta:
        model = Caregiver
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = '__all__'

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shifts
        fields = '__all__'