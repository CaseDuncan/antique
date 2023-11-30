from django.shortcuts import render
from django.http import HttpResponse
from users.forms import EvaluationRequestForm
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from users.models import Evaluation
from .forms import UserRegisterForm


#################### index####################################### 
def index(request):
	return render(request, 'index.html', {'title':'index'})

########### register here ##################################### 
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
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
		user = authenticate(request, username = username, password = password)
		print(user)
		if user is not None:
			form = login(request, user)
			messages.success(request, f' welcome {username} !!')
			return redirect('/')
		else:
			messages.info(request, f'account done not exit plz sign in')
	form = AuthenticationForm()
	return render(request, 'login.html', {'form':form, 'title':'log in'})

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