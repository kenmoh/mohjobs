from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from .models import Experience


# ADD EXPERIENCE
def add_experience(request):
    """ Add Experience """
    if request.method == 'POST':
        # Get form values
        user_id         = request.POST['user_id']
        company_name    = request.POST['company_name']
        job_title       = request.POST['job_title']
        year_from       = request.POST['year_from']
        year_to         = request.POST['year_to']
        job_description = request.POST['job_description']

        experience      = Experience(user_id=user_id, company_name=company_name, job_title=job_title, year_from=year_from, year_to=year_to, job_description=job_description)
        experience.save()

        messages.success(request, 'Experience added successfully. You may add more' )
        return redirect('experience')
    else:
        return render(request, 'experience/add_experience.html')

# EDIT EXPERIENCE
def edit_experience(request, id):
    """ This view is to edit user experience """
    experience = Experience.objects.get(pk=id)
    context = {
        'experience':experience
    }
    if request.method == 'POST':
        experience.user_id = request.POST['user_id' or None]
        experience.company_name = request.POST['company_name' or None]
        experience.job_title = request.POST['job_title' or None]
        experience.job_description = request.POST['job_description' or None]
        experience.year_from = request.POST['year_from' or None]
        experience.year_to = request.POST['year_to' or None]

        experience.save()
        messages.success(request, 'Experience Updated Successfully')
        return redirect('dashboard', experience.user_id)
    else:
        return render(request, 'experience/edit_experience.html', context)        

# DELETE EXPERIENCE
def delete_exp(request, id):
    experience = Experience.objects.all().get(pk=id)
    experience.delete()
    messages.success(request, 'Experience successfully deleted')
    return redirect('dashboard', experience.user_id)