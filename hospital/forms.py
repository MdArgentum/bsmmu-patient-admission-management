from django import forms
from .models import Patient, Contact

class PatientForm(forms.ModelForm):
    """Form definition for Patient."""

    class Meta:
        """Meta definition for Patientform."""
        model = Patient
        fields = '__all__'
        exclude = ['status']
        
    
    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs['placeholder'] = 'Enter Patient Name'
        for field_name, field in self.fields.items():
            # Add a CSS class to all fields
            field.widget.attrs['class'] = 'form-control'
            #field.widget.attrs['placeholder'] = f'Enter your {field_name.replace("_", " ")}'
        
    
class ContactForm(forms.ModelForm):
    """Form definition for Contact."""

    class Meta:
        """Meta definition for Contactform."""

        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'