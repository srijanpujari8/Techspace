from django import forms
from .models import Enquiry, BrochureLead


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['name', 'phone', 'email', 'course', 'branch', 'mode', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Full Name *',
                'required': True,
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Mobile Number *',
                'required': True,
                'pattern': '[6-9][0-9]{9}',
                'title': 'Enter a valid 10-digit Indian mobile number',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email Address',
            }),
            'course': forms.Select(attrs={'class': 'form-select'}),
            'branch': forms.Select(attrs={'class': 'form-select'}),
            'mode': forms.Select(attrs={'class': 'form-select'}),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Any specific question or requirement...',
                'rows': 3,
            }),
        }
        labels = {
            'name': 'Full Name',
            'phone': 'Mobile Number',
            'email': 'Email (optional)',
            'course': 'Course Interest',
            'branch': 'Preferred Branch',
            'mode': 'Learning Mode',
            'message': 'Message (optional)',
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '').strip()
        digits = ''.join(filter(str.isdigit, phone))
        if len(digits) < 10:
            raise forms.ValidationError('Enter a valid 10-digit mobile number.')
        return phone


class BrochureLeadForm(forms.ModelForm):
    class Meta:
        model = BrochureLead
        fields = ['name', 'phone', 'email']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Full Name *',
                'required': True,
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Mobile Number *',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email (optional)',
            }),
        }
