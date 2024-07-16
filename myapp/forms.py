from django.contrib.auth.models import User
from .models import Customer


from django import forms

# - Register/Create a user

class CreateUserForm(forms.Form):
     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-material', 'placeholder': 'Create Username'}))
     password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-material', 'placeholder': 'Create Password'}))
     password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-material', 'placeholder': 'Repeat Password'}))
     def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already taken.')
        return username

     def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Passwords do not match.')
        return cleaned_data

# Login form
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-material', 'placeholder': 'Enter Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-material', 'placeholder': 'Enter Password'}))

#add Customer
class CreateCustomerForm(forms.ModelForm):

    class Meta:

        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']


# - Update a Customer

class UpdateCustomerForm(forms.ModelForm):

    class Meta:

        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']