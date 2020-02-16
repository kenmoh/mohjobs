from django import forms
from django.core.exceptions import ValidationError
from account.models import UserProfile
from .models import UserProfile, User
from .states import STATE_CHOICES, STATUS_CHOICES
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control-sm ', 'Placeholder': 'First Name or Company Name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control-sm ', 'Placeholder': 'Last Name'}))
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control-sm ', 'Placeholder': 'Username'}))
    phone = forms.CharField(label='', widget=forms.NumberInput(
        attrs={'class': 'form-control-sm ', 'Placeholder': 'Phone Number'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'class': 'form-control-sm ', 'Placeholder': 'Email'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'form-control-sm ', 'Placeholder': 'Password', 'label': ''}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'form-control-sm ', 'Placeholder': 'Confirm Password', 'label': ''}))
    is_employer = forms.BooleanField(label='Employer')

    class Meta:
        model = User
        fields = ['first_name', 
                    'last_name',
                    'username',
                    'phone',
                    'email',
                    'password1',
                    'password2',
                    'is_employer'
    ]


    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if User.objects.filter(phone=phone).exists():
            raise ValidationError('A user with that Phone already exists.')
        return phone

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('A user with that Email already exists.')
        return email

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['last_name'].required = False  
        self.fields['is_employer'].required = False  
        

class UserProfileForm(forms.ModelForm):
    location = forms.ChoiceField(label='', choices=STATE_CHOICES, widget=forms.Select(
                              attrs={'class': 'form-control-sm '}))
    skills = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control-sm', 'Placeholder': 'Skills'}))
    about_me = forms.CharField(label='', required=True, widget=forms.Textarea(
        attrs={'rows': 2, 'class': 'form-control-sm hoverable', 'Placeholder': 'About Me'}))
    # profiele_image = forms.FileField(label='Profile Image')
    background_image = forms.ImageField(label='Background Image')
    # twitter = forms.CharField(label='', widget=forms.TextInput(
    #     attrs={'class': 'form-control-sm', 'Placeholder': 'Twitter'}))
    # github = forms.CharField(label='', widget=forms.TextInput(
    #     attrs={'class': 'form-control-sm', 'Placeholder': 'Github'}))
    # instagram = forms.CharField(label='', widget=forms.TextInput(
    #     attrs={'class': 'form-control-sm', 'Placeholder': 'Instagram'}))
    # facebook = forms.CharField(label='', widget=forms.TextInput(
    #     attrs={'class': 'form-control-sm', 'Placeholder': 'Facebook'}))
    # linkedin = forms.CharField(label='', widget=forms.TextInput(
    #     attrs={'class': 'form-control-sm', 'Placeholder': 'LinkedIn'}))
    # youtube = forms.CharField(label='', widget=forms.TextInput(
    #     attrs={'class': 'form-control-sm', 'Placeholder': 'YouTube'}))

    class Meta:
        model   = UserProfile
        fields  = ['location', 'skills', 'about_me', 'profile_image', 'background_image', 'publish']
       
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['location'].empty_label = 'Select Location'
        # self.fields['github'].required = False
        # self.fields['linkedin'].required = False
        # self.fields['twitter'].required = False
        # self.fields['youtube'].required = False
        # self.fields['facebook'].required = False
        # self.fields['instagram'].required = False
        self.fields['background_image'].required = False
        # self.fields['publish'].required = False


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={'class': 'form-control-sm', 'Placeholder': 'First Name'}))
    last_name = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={'class': 'form-control-sm', 'Placeholder': 'Last Name'}))
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control-sm', 'Placeholder': 'Username'}))
    phone = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control-sm', 'Placeholder': 'Phone Number'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'class': 'form-control-sm', 'Placeholder': 'Email'}))
    is_employer = forms.BooleanField(label='Employer')
    

    class Meta:
        model = User
        fields = ['first_name', 
                    'last_name',
                    'username',
                    'phone',
                    'email',
                    'is_employer'
    ]

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['last_name'].required = False  
        self.fields['is_employer'].required = False 
