from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from coding_profile.models import PlatformID

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile 
        fields = ['institute','yop','course','fullname','gender','city','state','image']
        
    
class EditPlatformIDForm(forms.ModelForm):

    class Meta:
        model = PlatformID
        fields = ['hackerRankID','codechefID','leetcodeID','codeforcesID','spojID']