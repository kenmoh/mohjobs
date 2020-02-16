from datetime import datetime
from django import template
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from account.models import User, UserProfile
from .models import JobPost
from .forms import JobPostForm, CompanyProfileForm
from account.states import STATUS_CHOICES, JOB_STATUS


def employer_profile(request, id=0):
    user = User.objects.get(pk=id)
  
    if request.method == 'GET':
        if id == user:
            form = CompanyProfileForm()
        else:
            user = UserProfile.objects.get(user_id=id)
            form = CompanyProfileForm(instance=user)
        return render(request, 'employers/company_profile_form.html', {'form': form})
    else:
        if id == user:
            form = CompanyProfileForm(request.POST, request.FILES)
        else:
            user = UserProfile.objects.get(user_id=id)
            form = CompanyProfileForm(request.POST, request.FILES, instance=user or None)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
        messages.success(request, 'Profile Upadated Successfully !')
        return redirect('employer-dashboard', request.user.pk)



def employer_dashboard(request, id):
    user    = get_object_or_404(User, pk=id)
    posts   = JobPost.objects.all().filter(user=user).order_by('-date_posted')
    context = {
        'user': user,
        'posts': posts,
    }

    return render(request, 'employers/dashboard.html', context)


def post(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            post_form = form.save(commit=False)
            post_form.user = request.user
            post_form.save()
            messages.success(request, 'Job Listed Successfuly')
            return redirect('employer-dashboard', request.user.pk)
        else:
            context = {
                'form':form
            }
            return render(request, 'employers/post.html', context)
    else:
        context = {
                'form':JobPostForm()
            }
        return render(request, 'employers/post.html', context)

def edit_post(request, id):
    job = get_object_or_404(JobPost, pk=id)
    if request.method == 'POST':
        form = JobPostForm(request.POST, instance=job)
        if form.is_valid():
            edited_form = form.save(commit=False)
            edited_form.user = request.user
            edited_form.save()
            messages.success(request, 'Job Updated Successfuly')
            return redirect('employer-dashboard', request.user.pk)
        else:
            context = {
                'form':form
            }
            return render(request, 'employers/post.html', context)
    else:
        context = {
                'form':JobPostForm(instance=job)
            }
        return render(request, 'employers/post.html', context)

def delete_job(request, id):
    jobpost = JobPost.objects.all().get(pk=id)
    jobpost.delete()
    messages.success(request, 'Job successfully deleted')
    return redirect('employer-dashboard', jobpost.user_id)


