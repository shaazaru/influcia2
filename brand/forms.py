from django import forms
from django.contrib.auth import get_user_model
from django.contrib import messages
from brand.models import MyUserManager, User
User = get_user_model()


class Brandregister(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields=('email', 'Business_Name', 'Business_Website', 'First_Name', 'Last_Name', 
        'Phone_Number', 'gridCheck', 'is_Brand')
        

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        self.cleaned_data['is_Brand'] = True

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    
    
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user