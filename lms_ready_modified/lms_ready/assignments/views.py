
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import AssignmentForm
from .models import Assignment

def is_teacher(user):
    return hasattr(user, 'profile') and user.profile.role in ['teacher','admin']

@login_required
def assignment_create(request, course_id):
    if not is_teacher(request.user):
        return HttpResponseForbidden()
    if request.method=='POST':
        form=AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            a=form.save(commit=False)
            a.created_by=request.user
            a.save()
            return redirect('course_detail', course_id)
    else:
        form=AssignmentForm()
    return render(request,'assignment_form.html',{'form':form})

@login_required
def assignment_edit(request, pk):
    a=Assignment.objects.get(pk=pk)
    if not is_teacher(request.user):
        return HttpResponseForbidden()
    if request.method=='POST':
        form=AssignmentForm(request.POST, request.FILES, instance=a)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form=AssignmentForm(instance=a)
    return render(request,'assignment_form.html',{'form':form})
