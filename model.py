# accounts/models.py
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

# service_requests/models.py
from django.db import models
from accounts.models import UserProfile

class RequestType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    request_type = models.ForeignKey(RequestType, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    submission_date = models.DateTimeField(auto_now_add=True)
    resolution_date = models.DateTimeField(null=True, blank=True)
    attached_file = models.FileField(upload_to='attachments/', null=True, blank=True)

    def __str__(self):
        return f"{self.request_type} - {self.status}"