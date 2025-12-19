from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Низький'),
        ('medium', 'Середній'),
        ('high', 'Високий'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    deadline = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    value = models.IntegerField()

    class Meta:
        unique_together = ('student', 'course')
