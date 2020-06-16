from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#inherits from usercreation form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() #default is required = True
    
    #keeps configs in one place, affects user model and saves data to the model
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
#create model form for user to upadte profile-update user model
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField() #default is required = True
    
    #for updating email
    class Meta:
        model = User
        fields = ['username', 'email']

#for updating image
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
    
