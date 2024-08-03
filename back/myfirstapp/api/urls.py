


from django.urls import path, include
from rest_framework import routers
from .views import EventViewSet, EventFundingViewSet, StudentParticipationViewSet, FeedbackViewSet, CertificateViewSet

post_router = routers.DefaultRouter()
post_router.register(r'events', EventViewSet)
post_router.register(r'eventfunding', EventFundingViewSet)
post_router.register(r'studentparticipation', StudentParticipationViewSet)
post_router.register(r'feedback', FeedbackViewSet)
post_router.register(r'certificate', CertificateViewSet)


urlpatterns = [
    # path('login/', login, name='login'),  # Add login endpoint
    path('', include(post_router.urls))
]





