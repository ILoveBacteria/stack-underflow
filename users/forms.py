from django import forms

from .models import User


class UserUpdateForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=255, widget=[forms.widgets.PasswordInput], disabled=True)
    password = forms.CharField(max_length=255, widget=[forms.widgets.PasswordInput], disabled=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'phone_number', 'national_id')
        error_messages = {
            'username': {
                'unique': 'This username is already exist!',
            },
        }

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).count():
            raise forms.ValidationError('This email is already exist!')
        return data


class UserRegisterForm(UserUpdateForm):
    confirm_password = forms.CharField(max_length=255, widget=[forms.widgets.PasswordInput])
    password = forms.CharField(max_length=255, widget=[forms.widgets.PasswordInput])

    def clean_password(self):
        data1 = self.cleaned_data['password']
        data2 = self.cleaned_data['confirm_password']
        if data1 != data2:
            raise forms.ValidationError('Password must match')
        if len(data1) == 0:
            raise forms.ValidationError('Enter the both of password')
        return data1
    
    def clean_confirm_password(self):
        data = self.cleaned_data['confirm_password']
        if len(data) == 0:
            raise forms.ValidationError('Enter the both of password')
        return data


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=[forms.widgets.PasswordInput])