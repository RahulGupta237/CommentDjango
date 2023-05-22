from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,TodoList,Item


class CustomUserCreationForm(UserCreationForm):
    name = forms.CharField(max_length=255)
    mobile_number = forms.CharField(max_length=20)
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ('name', 'mobile_number', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['name'].split()[0]
        user.last_name = self.cleaned_data['name'].split()[1]
        user.save()
        return user





class UserLogin(forms.ModelForm):
  email = forms.EmailField(max_length=255)
  class Meta:
    model = CustomUser
    fields = ['email', 'password']



class EditProfileForm(forms.ModelForm):
    password=None
    class Meta:
        model=CustomUser
        fields = ['email', 'name', 'mobile_number'] # Add additional fields as needed

        labels={'email':"Email"}





class EditAdminProfileForm(forms.ModelForm):
    password=None
    class Meta:
        model=CustomUser
        fields="__all__"
        labels={'email':"Email"}


class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['title', 'description', 'start_date', 'end_date', 'status', 'is_active']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class ItemForm(forms.ModelForm):
    todo = forms.ModelChoiceField(queryset=None, empty_label=None)

    class Meta:
        model = Item
        fields = ['item_title', 'todo', 'description', 'added_date']
        widgets = {
           
            'added_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, user, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['todo'].queryset = TodoList.objects.filter(user=user)


    



