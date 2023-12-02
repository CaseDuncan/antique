from django.shortcuts import render
from django.http import HttpResponse
from users.forms import EvaluationRequestForm
import os
from twilio.rest import Client
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm 
from users.models import Evaluation
from .forms import UserRegisterForm , VerificationCodeForm


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
        print(user)
        if user is not None:
            form = login(request, user)
            messages.success(request, f'Welcome {username} !!')
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
            return HttpResponse("form submited thanks")     

    else:
        form = EvaluationRequestForm()
        return render(request, "evaluation/request_evaluation.html", {"form": form})
    
def verification_view(request):
    form = VerificationCodeForm(request.POST or None)
    # pk = request.session.get('pk')
    # if pk:
    #     user = User.objects.get(pk=pk)
    #     code = user.code
    #     code_user = f"{user.username}: {code}"

    #     if not request.POST:
    #         #send SMS
    #         print(code_user)
    #         # send_SMS(code_user, user.phone_number)
    #     if form.is_valid():
    #             verification_code = form.cleaned_data.get('code')
    #             if str(code) == verification_code:
    #                 code.save()
    #                 login(request, user)
    #                 return redirect('/submit_evaluation')
    #             else:
    #                 return redirect('/login/')    
    return render(request, 'verify.html', {'form': form})