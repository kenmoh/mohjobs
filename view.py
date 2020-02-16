from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from account.models import User, UserProfile

from .models import Education, Experience
from account.states import STATE_CHOICES


# def user_details(request, id):

#     ''' Display One User Profile Details '''

#     user        = get_object_or_404(User, pk=id)
#     experiences = Experience.objects.all().filter(user=user)
#     educations  = Education.objects.all().filter(user=user)
#     context     = {
#         'user': user,
#         'experiences': experiences,
#         'educations': educations
#     }
#     return render(request, 'freelancer/user_details.html', context)


# def freelancer_dashboard(request, id):

#     """ Freelancer User Dashboard """
#     user        = get_object_or_404(User, pk=id)
#     experiences = Experience.objects.all().filter(user=user)
#     educations  = Education.objects.all().filter(user=user)
#     context     = {
#         'user': user,
#         'experiences': experiences,
#         'educations': educations
#     }
#     return render(request, 'freelancer/dashboard.html', context)

# def add_education(request):
#     """ Add Education """    
#     if request.method == 'POST':
#         # Get form Values
#         user_id         = request.POST['user_id']
#         school          = request.POST['school']
#         field_of_study  = request.POST['field_of_study']
#         qualification   = request.POST['qualification']
#         year            = request.POST['year']

#         education       = Education(user_id=user_id,school=school, field_of_study=field_of_study, qualification=qualification, year=year)
#         education.save()

#         messages.success(request, 'Eduction added successfully.' )
#         return redirect('freelancer:education')
#     else:
#         return render(request, 'freelancer/add_education.html')

# def edit_education(request, id):
#     """ This view is to edit user education"""
#     education = Education.objects.get(pk=id)
#     context = {
#         'education':education
#     }
#     if request.method == 'POST':
#         education.user_id           = request.POST['user_id' or None]
#         education.school            = request.POST['school' or None]
#         education.field_of_study    = request.POST['field_of_study' or None]
#         education.qualification     = request.POST['qualification' or None]
#         education.year              = request.POST['year' or None]

#         education.save()
#         messages.success(request, 'Education Updated Successfully')
#         return redirect('dashboard/%d'%request.user.id)
#     else:
#         return render(request, 'freelancer/edit_education.html', context)        


# def add_experience(request):
#     """ Add Experience """
#     if request.method == 'POST':
#         # Get form values
#         user_id         = request.POST['user_id']
#         company_name    = request.POST['company_name']
#         job_title       = request.POST['job_title']
#         year_from       = request.POST['year_from']
#         year_to         = request.POST['year_to']
#         job_description = request.POST['job_description']

#         experience      = Experience(user_id=user_id, company_name=company_name, job_title=job_title, year_from=year_from, year_to=year_to, job_description=job_description)
#         experience.save()

#         messages.success(request, 'Experience added successfully. You may add more' )
#         return redirect('freelancer:experience')
#     else:
#         return render(request, 'freelancer/add_experience.html')


# def edit_experience(request, id):
#     """ This view is to edit user experience """
#     experience = Experience.objects.get(pk=id)
#     context = {
#         'experience':experience
#     }
#     if request.method == 'POST':
#         experience.user_id = request.POST['user_id' or None]
#         experience.company_name = request.POST['company_name' or None]
#         experience.job_title = request.POST['job_title' or None]
#         experience.job_description = request.POST['job_description' or None]
#         experience.year_from = request.POST['year_from' or None]
#         experience.year_to = request.POST['year_to' or None]

#         experience.save()
#         messages.success(request, 'Experience Updated Successfully')
#         return redirect('dashboard/%d'%request.user.id)
#     else:
#         return render(request, 'freelancer/edit_experience.html', context)        


# Create and Edit User Profile
# def create_user_profile(request, id=0):

#     """User Profile Form"""
#     user = User.objects.get(pk=id)
  
#     if request.method == 'GET':
#         if id == user:
#             form = UserProfileForm()
#         else:
#             user = UserProfile.objects.get(user_id=id)
#             form = UserProfileForm(instance=user)
#         return render(request, 'freelancer/user_profile_form.html', {'form': form})
#     else:
#         if id == user:
#             form = UserProfileForm(request.POST, request.FILES)
#         else:
#             user = UserProfile.objects.get(user_id=id)
#             form = UserProfileForm(request.POST, request.FILES, instance=user)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = request.user
#             profile.save()
#         messages.success(request, 'Profile Upadate Successfully !')
#         return redirect('pages:index')

    


  
# def delete_exp(request, id):
#     experience = Experience.objects.all().get(pk=id)
#     experience.delete()
#     messages.success(request, f'Experience successfully deleted')
#     return redirect('dashboard/%d'%request.user.id)
  
# def delete_edu(request, id):
#     education = Education.objects.all().get(pk=id)
#     print(education.id)
#     education.delete()
#     messages.success(request, f'Education successfully deleted')
#     return reverse('dashboard/%d'%request.user.id)

def delete_user(request, id):
    user = User.objects.all().get(pk=id)
    user.delete()
    messages.success(request, f'Account with {user.username} deleted successfully')
    return redirect('pages:index')





# URLS
from django.urls import path
from . import views

urlpatterns = [
    # path('profile/<int:id>', views.user_details, name='profile'),
    # path('dashboard/<int:id>', views.freelancer_dashboard, name='dashboard'),
    # path('profile/update/<int:id>', views.create_user_profile, name='update'), 
    path('experience/add', views.add_experience, name='experience'),
    path('<int:id>', views.edit_experience, name='edit_experience'),
    path('delete/<int:id>', views.delete_user, name='delete'),
    path('delete/<int:id>', views.delete_exp, name='delete-exp'),
    path('delete/edu/<int:id>', views.delete_edu, name='delete_edu'),
    path('<int:id>', views.edit_education, name='edit_education'),
    path('education/add', views.add_education, name='education'),
  ]


# Admin
from django.contrib import admin
from .models import Education, Experience


# class UserProfileAdmin(admin.ModelAdmin):
#     pass
#     # list_display    = ['location', 'about_me', 'skills']
#     # list_filter     = ['location'] 
#     # search_fields   = ['skills', 'location'] 
    
class ExperienceAdmin(admin.ModelAdmin):
    
    list_display    = ['user','company_name', 'job_title', 'job_description']
    list_filter     = ['job_title'] 
    search_fields   = ['job_title'] 

class EducationAdmin(admin.ModelAdmin):
    
    list_display    = ['user', 'school', 'qualification', 'field_of_study']
    list_filter     = ['qualification', 'field_of_study'] 
    search_fields   = ['school', 'qualification', 'field_of_study']



admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
# admin.site.register(UserProfile, UserProfileAdmin)


# PAYSTACK
<form action="/process" method="POST" >
  <script
    src="https://js.paystack.co/v1/inline.js" 
    data-key="pk_test_221221122121"
    data-email="customer@email.com"
    data-amount="10000"
    data-ref=<UNIQUE TRANSACTION REFERENCE>
  >
  </script>
</form>