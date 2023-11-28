from django.shortcuts import render,redirect,HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def base(request):
    return render(request,'base_temp/basepage.html')

@login_required(login_url='login')
def users(request):
    data=User.objects.order_by('first_name')
    return render(request,'base_temp/userpage.html',{'userdata':data})

def form_view(request):
    form_obj=FormName()
    error=0
    error2=0
    if request.method=='POST':
        form=FormName(request.POST)
        if len(request.POST['name'])==2:
            error=1
        if request.POST.get('name').lower()=='amal':
            error2=1
        if form.is_valid():
            print('validation success')
            print(form.cleaned_data['name'])
    return render(request,'base_temp/form.html',{'form':form_obj,'error':error,'error2':error2})
    
def signup(request):
    form=UserForm()
    if request.method == 'POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return base(request)
    return render(request,'base_temp/signup.html',{'form':form})

def usersignup(request):
    registered=False

    if (request.method == 'POST'):
        user_form=AdminUserForm(request.POST)
        profile_form=UserProfileInfoForm(request.POST)
        #check validity
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()
            registered=True
        else:print(user_form.errors,profile_form.errors)
    
    else:
        user_form=AdminUserForm()
        profile_form=UserProfileInfoForm()

    return render(request,'base_temp/usersignup.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})


#login setup

def Log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect('basepage')
            else:
                return HttpResponse('account is not active')
        else:
            print('someone tried to login and failed')
            print('username:{} and password {}'.format(username,password))
            return HttpResponse('invalid login details supplied')
    
    else:
        return render(request,'base_temp/login_page.html')

@login_required(login_url='login')
def Log_out(request):
    logout(request)
    return render(request,'base_temp/basepage.html')