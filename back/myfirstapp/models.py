from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    
    # Define related_name for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_users',
        related_query_name='custom_user'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_users',
        related_query_name='custom_user'
    )

class Event(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    time = models.DateTimeField()
    date = models.DateField()
    summary = models.TextField()
    poster = models.ImageField(upload_to='event_posters/')
    approved = models.BooleanField(default=False)

class EventFunding(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='funding')
    item = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    date = models.DateField()
    proof = models.ImageField(upload_to='funding_proofs/')

class StudentParticipation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='participants')
    student_name = models.CharField(max_length=100)
    email = models.EmailField()

class Feedback(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    feedback_text = models.TextField()

class Certificate(models.Model):
    student_name = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateField()
