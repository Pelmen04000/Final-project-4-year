from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from courses.models import Course, Module, Lesson, Assignment, Grade
from django.utils import timezone

User = get_user_model()

class Command(BaseCommand):
    help = 'Create demo superuser and sample courses/modules/lessons'

    def handle(self, *args, **options):
        try:
            if not User.objects.filter(username='admin').exists():
                print('Creating superuser: admin / admin123')
                User.objects.create_superuser('admin', 'admin@example.com', 'admin123', role='admin')
            teacher, _ = User.objects.get_or_create(username='teacher1', defaults={'email':'teacher@example.com','role':'teacher'})
            student, _ = User.objects.get_or_create(username='student1', defaults={'email':'student@example.com','role':'student'})
            if not Course.objects.filter(slug='python-basics').exists():
                c = Course.objects.create(title='Python Basics', slug='python-basics', description='Intro course', created_by=teacher)
                m1 = Module.objects.create(course=c, title='Intro', order=1)
                l1 = Lesson.objects.create(module=m1, title='What is Python?', content='Python is ...', order=1)
                a1 = Assignment.objects.create(lesson=l1, title='Homework 1', description='Do something', due_date=timezone.now())
                Grade.objects.create(assignment=a1, student=student, score=95.0, feedback='Good job', graded_at=timezone.now())
                print('Created demo course: Python Basics')
            else:
                print('Demo course already exists')
        except Exception as e:
            print('Seeding failed:', e)
