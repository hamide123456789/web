from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms




class UserRegister(UserCreationForm):
    class Meta:
        model = User
        fields =['email', 'first_name', 'last_name', 'password1', 'password2']


    def clean_user_name(self):
        user = self.cleaned_data['user_name']
        if User.objects.filter(username = user).exists():
            raise forms.ValidationError('user exist')
        return user
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError('این ایمیل از قبل وجود دارد')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError('password not match')
        elif len(password2) < 8:
            raise forms.ValidationError('password to short')
        elif not any (x.isupper() for x in password2):
            raise forms.ValidationError('پسورد شما حداقل باید یک حروف بزرگ داشته باشد')
        return password1
    
class ProfileUpdateForm(forms.Form):
    class Meta:
        model = User
        fields =['user', 'phone', 'address']

class UserUpdateForm(forms.Form):
    class Meta:
        model = User
        fields =['user', 'phone', 'address']


class UserProfile(forms.Form):
    class Meta:
        model = User
        fields =['user', 'phone', 'address']



# class PhoneForm(forms.Form):
#     phone = forms.IntegerField()

# class CodeForm(forms.Form):
#     code =forms.IntegerField()
    







