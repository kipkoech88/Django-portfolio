from land.models import User 
from django import forms 

class UserForm(forms.ModelForm):
    name=forms.CharField(max_length=128, help_text="First Name") 
    address =forms.EmailField(help_text="Email Adress") 
    message=forms.CharField(widget=forms.Textarea, max_length=600, help_text="Message") 

    class Meta:
        model=User 
        fields=('name',)