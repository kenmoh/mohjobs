from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from .models import User, UserProfile
from .forms import UserProfileForm, RegistrationForm, UserUpdateForm
from education.models import Education
from experience.models import Experience
from .states import status_choices




# REGISTER
    
def register(request):
    """User Registeration """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Account created Successfully ! You can now Login')
            return redirect('login')

    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})
    
# LOGIN
def login_view(request):
    if request.method == 'POST':
        username        = request.POST['username']
        password        = request.POST['password']

        user            = auth.authenticate(username=username, password=password) 

        # Check if user is in database
        if user is not None and user.is_employer:
            auth.login(request, user)
            messages.success(request, 'You are now logged in. Click on the dashboard tab to update your profile')
            return redirect('index') 
        elif user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in. Click on the dashboard tab to update your profile')
            return redirect('dashboard', user.id)
        else:
            messages.error(request, 'Invalid Credentials, Check username or password')
            return redirect('login') 
    else:
        return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

# CHANGE USER
def change_user(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST or None, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'User Updated Successfully !')
            if request.user.is_employer:
                return redirect('employer-dashboard', request.user.id)
            else:
                return redirect('dashboard', request.user.id)
    else:
        form = UserUpdateForm(instance=request.user)

    context = {
        'form': form
    }

    return render(request, 'accounts/update.html', context)


# DASHBOARD
def freelancer_dashboard(request, id):

    """ Freelancer User Dashboard """
    
    user        = get_object_or_404(User, pk=id)
    experiences = Experience.objects.all().filter(user=user)
    educations  = Education.objects.all().filter(user=user)
    context     = {
        'user': user,
        'experiences': experiences,
        'educations': educations
    }
    return render(request, 'accounts/dashboard.html', context)

# USER DETAILS
def user_details(request, id):

    ''' Display One User Profile Details '''

    user        = get_object_or_404(User, pk=id)
    experiences = Experience.objects.all().filter(user=user)
    educations  = Education.objects.all().filter(user=user)
    context     = {
        'user': user,
        'experiences': experiences,
        'educations': educations
    }
    return render(request, 'accounts/user_details.html', context)

# CREATE USER PROFILE
def create_user_profile(request, id=0):

    """User Profile Form"""
    user = User.objects.get(pk=id)
  
    if request.method == 'GET':
        if id == user:
            form = UserProfileForm()
        else:
            user = UserProfile.objects.get(user_id=id)
            form = UserProfileForm(instance=user)
        return render(request, 'accounts/user_profile_form.html', {'form': form})
    else:
        if id == user:
            form = UserProfileForm(request.POST, request.FILES)
        else:
            user = UserProfile.objects.get(user_id=id)
            form = UserProfileForm(request.POST, request.FILES, instance=user or None)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
        messages.success(request, 'Profile Upadated Successfully !')
        return redirect('index')

# DELETE USER
def delete_user(request, id):
    user = User.objects.all().get(pk=id)
    user.delete()
    messages.success(request, f'Account with {user.username} deleted successfully')
    return redirect('index')

