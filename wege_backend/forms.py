from django import forms
from .models import UserInfoTable


class RegistrationForm(forms.ModelForm):
    ''' 
       This form object use in signup form
    '''
    class Meta:
        model = UserInfoTable
        fields = [
            'username',
            'email',
            'password',
        ]

        labels = {"username":'','email':'','password':''}
    
        widgets = {

            'username': forms.TextInput(attrs={'class': 'login_field', 'placeholder': 'Enter your username'}),
            'email': forms.EmailInput(attrs={'class': 'login_field', 'placeholder': 'Enter your email id'}),
            'password':forms.PasswordInput(attrs={'class': 'login_field', 'placeholder': 'Enter  your password'}),

        }


    def save(self, commit=True):
        '''
         This method encrypt plaintext password before creating new user into the database
        '''
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()

        return user



class LoginForm(forms.ModelForm):
    '''
    This form object use in login form
    '''
    class Meta:
        model = UserInfoTable
        fields = [
            'username',
            'password',
        ]

        labels = {"username":'','password':''}
    
        widgets = {

            'username': forms.TextInput(attrs={'class': 'login_field', 'placeholder': 'Enter your username'}),
            'password':forms.PasswordInput(attrs={'class': 'login_field', 'placeholder': 'Enter  your password'}),

        }