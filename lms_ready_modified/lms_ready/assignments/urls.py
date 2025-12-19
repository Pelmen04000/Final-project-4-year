
from django.urls import path
from . import views

urlpatterns=[
    path('<int:course_id>/create/', views.assignment_create, name='assignment_create'),
    path('<int:pk>/edit/', views.assignment_edit, name='assignment_edit'),
]
