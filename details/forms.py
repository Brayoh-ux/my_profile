from django import forms
from .models import Profile, Pictures
from cloudinary.models import CloudinaryField

class ProfileForm(forms.ModelForm):
    """Form definition for Profile."""

    class Meta:
        """Meta definition for Profileform."""

        model = Profile
        fields = ('email', 'image', 'contact_me')

class PicturesForm(forms.ModelForm):
    """Form definition for Profile."""

    class Meta:
        """Meta definition for Profileform."""

        model = Pictures
        fields = ('project_1', 'project_2', 'project_3',
                    'project_4', 'project_5', 'project_6',
                    'project_7')

class LetterForm(forms.Form):
    """LetterForm definition."""
    your_name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Email')
    text = forms.CharField()
