from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from .models import JobPost
from account.models import UserProfile
from account.states import STATE_CHOICES, JOB_STATUS

class CompanyProfileForm(ModelForm):  
    location = forms.ChoiceField(label='Location', choices=STATE_CHOICES, widget=forms.Select(
                              attrs={'class': 'form-control-sm '}))

    website = forms.URLField(label='', widget=forms.URLInput(
        attrs={'class': 'form-control-sm', 'Placeholder': 'Website'}))

    # profiele_image = forms.FileField(label='Profile Image')
    background_image = forms.ImageField(label='Background Image')
    
    
    class Meta:
        model = UserProfile
        fields = [
            
            'website',
            'location',
            'profile_image',
            'background_image',
        ]
    def __init__(self, *args, **kwargs):
        super(CompanyProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['location'].empty_label = 'Select Location'
        self.fields['website'].required = False
        self.fields['profile_image'].required = False
        self.fields['background_image'].required = False


class JobPostForm(ModelForm):
    job_title = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control-sm', 'Placeholder': 'Job Title'}))
    job_requirement = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control-sm', 'Placeholder': 'Required Skill(s) | Seperate Skills with Comma.'}))

    years_experience = forms.IntegerField(label='', widget=forms.NumberInput(
        attrs={'class': 'form-control-sm', 'Placeholder': 'Year(s) of Experience'}))

    job_description = forms.CharField(label='', required=True, widget=forms.Textarea(
        attrs={'rows': 2, 'class': 'form-control-sm', 'Placeholder': 'Job Dscription'}))
        
    job_location = forms.ChoiceField(label='Location', choices=STATE_CHOICES, widget=forms.Select(
                              attrs={'class': 'form-control-sm '}))
    application_link = forms.URLField(label='', widget=forms.URLInput(
        attrs={'class': 'form-control-sm', 'Placeholder': 'Application Link'}))

    application_email = forms.EmailField(label='', required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control-sm', 'Placeholder': 'Application Email'}))
    
    publish = forms.BooleanField(label='Publish')
    

    class Meta:
        model = JobPost
        fields = (
            'job_title',
            'job_requirement',
            'years_experience',
            'job_description',
            'job_location',
            'application_link',
            'application_email',
            'publish'
        )

    def __init__(self, *args, **kwargs):
        super(JobPostForm, self).__init__(*args, **kwargs)
        self.fields['job_location'].empty_label = 'Select Location'
        self.fields['application_email'].required = False
        self.fields['application_link'].required = False
        self.fields['publish'].required = False