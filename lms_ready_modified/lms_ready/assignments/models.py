from django.db import models
from django.conf import settings

PRIORITY_CHOICES = [
    ('low', 'Low'),
    ('mid', 'Mid'),
    ('high', 'High'),
]

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='assignments/', blank=True, null=True)
    deadline = models.DateTimeField()
    priority = models.CharField(max_length=5, choices=PRIORITY_CHOICES, default='low')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
