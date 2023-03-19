from rest_framework import serializers
from .models import Athlete


class AthleteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    coach = serializers.ReadOnlyField(source='coach.id')

    class Meta:
        model = Athlete
        fields = ['id', 'first_name', 'last_name', 'ethnicity', 'sex', 'weight', 'height', 'blood_type', 'sport',
                  'phone', 'email', 'contact_method', 'coach', 'athlete_image']
