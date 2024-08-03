from django.contrib import admin
from .models import CustomUser, Event, EventFunding, StudentParticipation, Feedback, Certificate

admin.site.register(CustomUser)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'time', 'date', 'summary', 'user', 'approved')
    list_filter = ('approved',)
    search_fields = ('name', 'summary', 'user__username')
    date_hierarchy = 'date'
    ordering = ('-date',)

@admin.register(EventFunding)
class EventFundingAdmin(admin.ModelAdmin):
    list_display = ('item', 'cost', 'quantity', 'date', 'event')
    search_fields = ('item', 'event__name')
    date_hierarchy = 'date'
    ordering = ('-date',)

@admin.register(StudentParticipation)
class StudentParticipationAdmin(admin.ModelAdmin):
    list_display = ('event', 'student_name', 'email')
    search_fields = ('event__name', 'student_name', 'email')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('event', 'student_name', 'feedback_text')
    search_fields = ('event__name', 'student_name', 'feedback_text')

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'event', 'date')
    search_fields = ('student_name', 'event__name')
    date_hierarchy = 'date'
    ordering = ('-date',)
