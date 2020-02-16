from django import forms
from account.states import STATE_CHOICES, STATUS_CHOICES
from account.models import User, UserProfile


class LekkiForm(forms.ModelForm):
    lekki = forms.BooleanField(label='Confirm Payment', required=False)

    class Meta:
        model = User
        fields = ['lekki']


class IkoyiForm(forms.ModelForm):
    ikoyi = forms.BooleanField(label='Confirm Payment', required=False)

    class Meta:
        model = User
        fields = ['ikoyi']


class EkoForm(forms.ModelForm):
    eko_atlantic = forms.BooleanField(label='Confirm Payment', required=False)

    class Meta:
        model = User
        fields = ['eko_atlantic']


class SearchForm(forms.ModelForm):
    location = forms.ChoiceField(label='Location', choices=STATE_CHOICES, widget=forms.Select(
        attrs={'class': 'form-control-sm'}))
    skills = forms.CharField(label='Skills', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control-sm', 'Placeholder': 'Skills'}))

    class Meta:
        model = UserProfile
        fields = ['skills', 'location']

          
    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['location'].empty_label = 'Select Location'
        self.fields['skills'].required = False
        self.fields['location'].required = False