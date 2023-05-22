from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    name = forms.CharField(max_length=255)
    mobile_number = forms.CharField(max_length=20)
    email = forms.EmailField()
    profile_photo=forms.ImageField(required=True)
    

    class Meta:
        model = CustomUser
        fields = ['name', 'mobile_number', 'profile_photo', 'email', 'password1', 'password2']

   
    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.profile_photo = self.cleaned_data['profile_photo']
        if commit:
            user.save()
        return user





class UserLogin(forms.ModelForm):
  email = forms.EmailField(max_length=255)
  
  password = forms.CharField(widget=forms.PasswordInput)
  class Meta:
    model = CustomUser
    fields = ['email', 'password']