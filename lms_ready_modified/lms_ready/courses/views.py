from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Course
from .forms import CourseForm

def user_is_teacher_or_admin(user):
    try:
        role = getattr(user, 'profile').role
    except Exception:
        role = None
    return role in ('teacher', 'admin')

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'course_detail.html', {'course': course})

@login_required
def course_create(request):
    if not user_is_teacher_or_admin(request.user):
        return HttpResponseForbidden("Только teacher или admin могут создавать курс.")
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES or None)
        if form.is_valid():
            course = form.save(commit=False)
            
            course.save()
            return redirect('course_detail', course_id=course.id)
    else:
        form = CourseForm()
    return render(request, 'course_form.html', {'form': form, 'action': 'create'})

@login_required
def course_edit(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if not user_is_teacher_or_admin(request.user):
        return HttpResponseForbidden("Только teacher или admin могут редактировать курс.")
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES or None, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_detail', course_id=course.id)
    else:
        form = CourseForm(instance=course)
    return render(request, 'course_form.html', {'form': form, 'action': 'edit', 'course': course})

@login_required
def course_delete(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if not user_is_teacher_or_admin(request.user):
        return HttpResponseForbidden("Только teacher или admin могут удалять курс.")
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'course_confirm_delete.html', {'course': course})
