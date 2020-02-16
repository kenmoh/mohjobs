from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from .models import Education


# ADD EDUCATION
def add_education(request):
    """ Add Education """    
    if request.method == 'POST':
        # Get form Values
        user_id         = request.POST['user_id']
        school          = request.POST['school']
        field_of_study  = request.POST['field_of_study']
        qualification   = request.POST['qualification']
        year            = request.POST['year']

        education       = Education(user_id=user_id, school=school, field_of_study=field_of_study, qualification=qualification, year=year)
        education.save()

        messages.success(request, 'Eduction added successfully.' )
        return redirect('education')
    else:
        return render(request, 'education/add_education.html')


# EDIT EDUCATION
def edit_education(request, id):
    """ This view is to edit user education"""
    education = Education.objects.get(pk=id)
    context = {
        'education':education
    }
    if request.method == 'POST':
        education.user_id           = request.POST['user_id' or None]
        education.school            = request.POST['school' or None]
        education.field_of_study    = request.POST['field_of_study' or None]
        education.qualification     = request.POST['qualification' or None]
        education.year              = request.POST['year' or None]

        education.save()
        messages.success(request, 'Education Updated Successfully, you may add another !')
        return redirect('dashboard', education.user_id)
    else:
        return render(request, 'education/edit_education.html', context)        


# DELETE EDUCATION
def delete_edu(request, id):
    education = Education.objects.all().get(pk=id)
    education.delete()
    messages.success(request, f'Education successfully deleted')
    return redirect('dashboard', education.user_id)
