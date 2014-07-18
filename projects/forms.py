from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from models import *


class ProjectUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

    def clean_username(self):
            username = self.cleaned_data["username"]
            try:
                User.objects.get(username=username)
            except User.DoesNotExist:
                return username
            raise forms.ValidationError(
                self.error_messages['duplicate_username'],
                code='duplicate_username',
            )


class CompanyForm(ModelForm):
    class Meta:
        model = Company


class ProjectForm(ModelForm):
    class Meta:
        model = Project


class DeveloperForm(ModelForm):
    class Meta:
        model = Developer


class UserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "password")

