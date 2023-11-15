from django import forms

from .models import User


class UserUpdateForm(forms.ModelForm): 
    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'national_id')
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


class UserRegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=255, widget=forms.widgets.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'national_id', 'password', 'confirm_password')
        error_messages = {
            'username': {
                'unique': 'This username is already exist!',
            },
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        email = cleaned_data['email']
        if password != confirm_password:
            raise forms.ValidationError('Password must match')
        if len(password) == 0 or len(confirm_password) == 0:
            raise forms.ValidationError('Enter the both of password')
        if User.objects.filter(email=email).count():
            raise forms.ValidationError('This email is already exist!')
        return cleaned_data


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=255, widget=forms.widgets.PasswordInput)