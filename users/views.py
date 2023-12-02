import json
from django.shortcuts import render
from django.http import HttpResponse
from users.forms import EvaluationRequestForm
import os
from twilio.rest import Client
# Create your views here.

from django.shortcuts import render, redirect , get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm 
from users.models import Evaluation , CustomUser , VerificationCode
from .forms import UserRegisterForm , VerificationCodeForm
from .utils import send_SMS


#################### index####################################### 
def index(request):
	return render(request, 'index.html', {'title':'index'})

########### register here ##################################### 
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data.get('phone_number')
            print(phone)
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('/login')
    else:
        form = UserRegisterForm()

    return render(request, 'Register.html', {'form': form, 'title': 'Register Here'})

################ login forms################################################### 

def Login(request):
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user.is_verified)

        if user is not None:
            form = login(request, user)
            messages.success(request, f'Welcome {username} !!')
            userId = request.user.id
            verificationCodeRecord = VerificationCode.objects.get(user_id = userId)
            send_SMS(verification_code=verificationCodeRecord.code , phone_number='+254758262427')
            return redirect('/verify')
        else:
            messages.info(request, 'Account does not exist, please sign in')

    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'title': 'log in'})


def evaluation(request):
    # print(request.user)
    return render(request , 'evaluation/request_evaluation.html')

def create_evaluation(request):
    form = EvaluationRequestForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            user = request.user
   
            evaluation_request = form.save(commit=False)
            evaluation_request.user = request.user
            evaluation_request.save()
            # Evaluation.objects.create(user_id = user.id , comment = form.cleaned_data.get('comment') , contact_method = form.cleaned_data.get('contact_method') , antique_img=request.FILES)
            return redirect('/create_evaluation')    

    else:
        form = EvaluationRequestForm()
        return render(request, "evaluation/request_evaluation.html", {"form": form})

@login_required
def verification_view(request):
    errMsg = ""
    form = VerificationCodeForm(request.POST or None)
    user = request.user 
    body_unicode = request.body.decode('utf-8')
    checkIfUserIsVerified = CustomUser.objects.get(id=user.id)
    if checkIfUserIsVerified.is_verified:
        return redirect("/evaluation")
    if request.POST:
        code = body_unicode.split('&')[1].split("=")[1]
        verifCode = VerificationCode.objects.get(user_id=user.id)
        if verifCode.code == code:
            editUser = CustomUser.objects.get(id=user.id)
            editUser.is_verified = True
            editUser.save()
            return redirect("/evaluation")
        else:

            errMsg = "Incorrect Verification Code"
   
    return render(request, 'verify.html', {'form': form , 'errMsg' : errMsg})

@login_required
def evaluation_listings(request):
    listings = Evaluation.objects.all()
    return render(request , 'evaluation/evaluation_listing.html' ,{'listings' : listings})