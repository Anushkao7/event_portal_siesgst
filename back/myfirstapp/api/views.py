from rest_framework import viewsets
from ..models import Event, EventFunding, StudentParticipation, Feedback, Certificate
from .serializers import EventSerializer, EventFundingSerializer, StudentParticipationSerializer, FeedbackSerializer, CertificateSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventFundingViewSet(viewsets.ModelViewSet):
    queryset = EventFunding.objects.all()
    serializer_class = EventFundingSerializer

class StudentParticipationViewSet(viewsets.ModelViewSet):
    queryset = StudentParticipation.objects.all()
    serializer_class = StudentParticipationSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
