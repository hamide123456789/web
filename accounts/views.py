from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import UserRegister , ProfileUpdateForm , UserUpdateForm, UserProfile 
# from .forms import PhoneForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .models import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
# from random import randint , CodeForm
# import ghasedak
#authenticateمیاد بررسی میکنه اطلاعاتی که کاربر وارد دیتا بیس وارد کرده وجود داره یاخیر






def register(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home:home')
    else:
        form = UserRegister()
    return render(request, 'register.html', {'form':form})
    
def user_login(request):
    if request.method =='POST':
        try:
            user = authenticate(request, email=request.POST.get('email'), password=request.POST.get('password'))
        except:
            user = authenticate(request, email=request.POST.get('email'), password=request.POST.get('password'))
    
        if user is not None:
            login(request,user)
            messages.success(request,'wellcome my site','primary')
            return redirect('home:home')
        else:
            messages.error(request,'email or password wrong','danger')
    return render(request, 'login.html')



def user_logout(request):
    logout(request)
    messages.success(request,'باموفقیت خارج شدید','warning')
    return redirect('home:home')


@login_required(login_url='accounts:login')
def user_profile(request):
    print(request.user.id)
    user = User.objects.all()
    print(user)
    user = User.objects.get(id=request.user.id)
    profile = UserProfile.objects.get(user=user)
    return render(request,'profile.html',{'profile':profile}) 


@login_required(login_url='accounts:login')
def user_update(request):
    if request.method == 'POST':
        user_from = UserUpdateForm(request.POST , instance=request.user)
        profile_form =ProfileUpdateForm(request.POST, instance=request.user.profile)
        if user_from and profile_form.is_valid():
            user_from.save()
            profile_form.save()
            messages.success(request,'update successfuly','success')
            return redirect('accounts:home')
    else:
       user_from = UserUpdateForm(instance=request.user)
       profile = UserProfile.objects.get(user = request.user)
       profile_form =ProfileUpdateForm(instance=profile)
    context ={'user_form':user_from ,'profile_form':profile_form}
    return render(request,'update.html',context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user , request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,'پسورد با موفقیت تغییرکرد','success')
            return redirect('accounts:profile')
        else:
            messages.error(request,'پسورد اشتباه است','danger')
            return redirect('accounts:change')
    else:
        form = PasswordChangeForm(request.user)
        return render(request ,'change.html',{'form':form})
    


# def phone(request):
#     if request.method == 'POST':
#         form = PhoneForm(request.POST)
#         if form.is_valid():
#             global random_code ,phone
#             data = form .cleaned_data
#             phone = f"0{data['phone']}"
#             random_code = randint(100,1000)
#             sms = ghasedak.Ghasedak('')
#             sms.send({'message':random_code , 'receptor':phone , 'linenumber':10008566})
#             return redirect('accounts:verify')
#     else:
#         form = PhoneForm
#     return render(request,'phone.html',{'form':form})

# def verify(request):
#     if request.method == 'POST':
#         form = CodeForm(request.post)
#         if form.is_valid():
#             if random_code == form.cleaned_data['code']:
#                 profile = profile.objects.get(phone = phone)
#                 user = user.objects.get(profile__id = profile.id)
#                 login(request,user)
#                 messages.success(request,'hi user')
#                 return redirect('home:home')
#             else:
#                 messages.error(request,'code warning')
#     return render(request,'code.html')
