from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.models import User, UserProfile
from account.states import LOCATION_CHOICES, STATE_CHOICES
from employers.models import JobPost
from .forms import LekkiForm, IkoyiForm, EkoForm
from .models import Contact


# Home Page
def index(request):
    """ Display all the Users """
    users = User.objects.all()
 
    context = {
        'users': users,
        'location': LOCATION_CHOICES,
    } 
    return render(request, 'pages/index.html', context)

# Search Applicants/Freelancers
def search(request):
    ''' Search by Location and Skills '''
    users = User.objects.filter(is_employer=False)

  # Keywords
    if 'skills' in request.GET:
        skills = request.GET['skills']
        if skills:
            users = users.distinct().filter(userprofile__skills__icontains=skills)

    # State
    if 'location' in request.GET:
        location = request.GET['location']
        if location:
            users = users.distinct().filter(userprofile__location__iexact=location)

    context = {
        'users':users,
        'location': LOCATION_CHOICES,
        'values': request.GET
    }

    return render(request, 'pages/search.html', context)

# Search Job Listings
def job_search(request):
    ''' Search by Location and Skills '''
    jobs = JobPost.objects.all().order_by('-date_posted').filter(publish=True)
  # Keywords
    if 'job_requirement' in request.GET:
        job_requirement = request.GET['job_requirement']
        if job_requirement:
            jobs = jobs.filter(job_requirement__icontains=job_requirement)

    # State
    if 'job_location' in request.GET:
        job_location = request.GET['job_location']
        if job_location:
            jobs = jobs.filter(job_location__iexact=job_location)

    context = {
        'jobs':jobs,
        'job_location': LOCATION_CHOICES,
        'values': request.GET
    }
    return render(request, 'pages/job_search.html', context)


# About Us page
def about(request):
    return render(request, 'pages/about.html')


# Contact Us page
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['subject']

        contact_us = Contact(name=name.title(), email=email, subject=subject, message=message)
        contact_us.save()

        messages.success(request, 'Message sent successfully. We will get back to you shortly !' )
        return redirect('index')
    else:
        return render(request, 'pages/contact.html')

# Pricing Page
def pricing(request):
    return render(request, 'pages/pricing.html')


# Post Job
def job(request):
    """ Display all Job Listings """
    jobs = JobPost.objects.all().order_by('-date_posted').filter(publish=True)
    context = {
        'jobs': jobs,
        'job_location': LOCATION_CHOICES,
        
    } 
    return render(request, 'pages/jobs.html', context)

# View Job Details
def job_detail(request, id):
    """ Display all Job Listings """
    posts   = JobPost.objects.filter(pk=id)
    context = {
        'posts': posts,
    }
    return render(request, 'employers/job_description.html', context)

# Paystack Redirect
@login_required
def confirm_lekki(request):
    return render(request, 'pages/confirm_lekki.html')

@login_required
def confirm_ikoyi(request):
    return render(request, 'pages/confirm_ikoyi.html')

@login_required
def confirm_eko(request):
    return render(request, 'pages/confirm_eko.html')

# Update Plan
@login_required
def lekki_update(request):
    if request.method == 'POST':
        form = LekkiForm(request.POST or None, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Subscription Successful !')
            return redirect('employer-dashboard', request.user.id)
    else:
        form = LekkiForm(instance=request.user)
    context = {
        'form': form
    }

    return render(request, 'pages/lekki.html', context)
@login_required
def ikoyi_update(request):
    if request.method == 'POST':
        form = IkoyiForm(request.POST or None, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Payment Updated Successfully !')
            return redirect('employer-dashboard', request.user.id)
    else:
        form = IkoyiForm(instance=request.user)
    context = {
        'form': form
    }

    return render(request, 'pages/ikoyi.html', context)
@login_required
def eko_update(request):
    if request.method == 'POST':
        form = EkoForm(request.POST or None, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Payment Updated Successfully !')
            return redirect('employer-dashboard', request.user.id)
    else:
        form = EkoForm(instance=request.user)

    context = {
        'form': form
    }

    return render(request, 'pages/eko.html', context)

