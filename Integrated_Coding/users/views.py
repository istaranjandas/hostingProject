from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .form import UserRegisterForm, EditProfileForm,EditPlatformIDForm
from django.contrib.auth.decorators import login_required
from verify_email.email_handler import send_verification_email


def index(request):
    return render(request,'index.html')

@login_required
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            inactive_user = send_verification_email(request, form)
            username=form.cleaned_data.get('username')
            messages.info(request,f'A mail is send to your registered mail id for verification')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'register.html',{'form':form})

@login_required
def profile(request):
    if request.method=='POST':
        form = EditPlatformIDForm(request.POST,instance=request.user.platformid)
        if form.is_valid():
            form.save()
            messages.success(request,f'Your PlatformID has been updated...')
            return redirect('profile-page')
    else:
        form=EditPlatformIDForm(instance=request.user.platformid)
    return render(request,'profile.html',{'form':form})

@login_required
def edit_profile(request):
    if request.method=='POST':
        form=EditProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request,f'Your profile has been updated...')
            return redirect('profile-page')
    else:
        form=EditProfileForm(instance=request.user.profile)
    return render(request,'edit_profile.html',{'form':form})

@login_required
def view_profile(request, username):
    view_user= User.objects.get(username=username)
    return render(request, 'view_profile.html', {'view_user':view_user})

