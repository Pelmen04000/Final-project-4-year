from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from .models import Course, Grade
from .utils import is_teacher_or_admin

def register(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        group, _ = Group.objects.get_or_create(name='student')
        user.groups.add(group)
        return redirect('login')
    return render(request, 'auth/register.html')


@login_required
def course_list(request):
    return render(request, 'courses/course_list.html', {
        'courses': Course.objects.all()
    })


@login_required
@user_passes_test(is_teacher_or_admin)
def course_create(request):
    if request.method == 'POST':
        Course.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            priority=request.POST['priority'],
            deadline=request.POST['deadline'],
            created_by=request.user
        )
        return redirect('course_list')
    return render(request, 'courses/course_form.html')


@login_required
@user_passes_test(is_teacher_or_admin)
def journal(request):
    if request.method == 'POST':
        Grade.objects.update_or_create(
            student_id=request.POST['student'],
            course_id=request.POST['course'],
            defaults={'value': request.POST['grade']}
        )

    return render(request, 'courses/journal.html', {
        'grades': Grade.objects.all(),
        'students': User.objects.filter(groups__name='student'),
        'courses': Course.objects.all()
    })
