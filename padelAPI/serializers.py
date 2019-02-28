from rest_framework import serializers
from padelAPI.models import Court, Reservation


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'user',
            'start_date',
            'end_date',
            'court',
            'created_at',
        )
        model = Reservation
