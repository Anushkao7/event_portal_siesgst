from rest_framework import serializers
from ..models import Event, EventFunding, StudentParticipation, Feedback, Certificate 

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class EventFundingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventFunding
        fields = '__all__'

class StudentParticipationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentParticipation
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'
