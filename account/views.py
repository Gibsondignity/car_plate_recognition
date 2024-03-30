from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .forms import RegisterForm, SecurityQuestionForm
from .models import Acount_User
from django.http import JsonResponse
from account.models import *



# Create your views here.
def account_login(request):
    if request.user.is_authenticated:
        #return redirect(reverse('dashboard'))
        messages.error(request, 'You are already logged in')
    if request.method == 'POST':
        
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            security_question = SecurityAnswer.objects.filter(user=request.user).first()
            if not request.user.phone or not request.user.first_name or not request.user.second_name or not security_question:
                messages.success(request, "Please finish setting up your profile!")
                return redirect(reverse('profile'))
            else: 
                messages.success(request, 'Login Successful')
                return redirect(reverse('home'))
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'account/login.html')




def account_logout(request):
    logout(request)
    return redirect(reverse('accounts'))




# user roles and permissions 
def register(request):
    form = RegisterForm(request.POST or None)
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        user = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect(reverse('register'))
        
        
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            
            messages.success(request, 'User created successfully')
            messages.success(request, 'Setup your profile')
            login(request, user)
            return redirect(reverse('profile'))
        else:
            messages.error(request, form.errors.as_text())
            
    
    
    context = {'form': form, }
    return render(request, 'account/register.html', context)





def reset_password(request):
    form = SecurityQuestionForm()
    security_questions = SecurityQuestion.objects.all()
    # print(request.user.securityanswer.question)
    # print(request.user.securityanswer.answer_text)
    
    if request.method == "POST":
        security_question = request.POST.get("security_question")
        answer =  request.POST.get("answer")
        
        security_answer = SecurityAnswer.objects.filter(question=security_question, answer_text=answer)
        if security_answer.exists():
            if len(security_answer) == 1:
                security_answer = security_answer.first()
                user_id = security_answer.user.id
                user = security_answer.user
                context = {"user_id":user_id, "user":user}
                return render(request, "account/new_password.html", context)
            else:
                context = {'security_question':security_question, 'answer':answer}
                messages.warning(request, "Two or more users returned, enter a contact number to confirm identity")
                return render(request, 'account/enter_number.html', context)
        else:
            messages.error(request, "Sorry, user not found")
            return redirect(reverse('reset_password'))
    context = {"security_form": form, "security_questions":security_questions}
    return render(request, 'account/reset_password.html', context)




def enter_number(request):
    
    context = {}
    if request.method == "POST":
        security_question = request.POST.get("security_question")
        answer =  request.POST.get("answer")
        contact = request.POST.get("contact")
        user = Acount_User.objects.filter(phone=contact).first()
        security_answer = SecurityAnswer.objects.filter(user=user)
        try:
            if security_answer.exists():
                user_id = user.id
                context = {"user_id":user_id, "user":user}
                return render(request, "account/new_password.html", context)
            else:
                messages.error(request, "Sorry, user not found")
                return redirect(reverse('reset_password'))
        except:
            messages.error(request, "Sorry, user not found")
            return redirect(reverse('reset_password'))
            
    return render(request, 'account/enter_number.html', context)





def new_password(request):
    
    if request.method ==  "POST":
        user = request.POST.get("user_id")
        password = request.POST.get("password")
        
        user = Acount_User.objects.get(id=user)
        user.set_password(password)
        user.save()
        return redirect(reverse('accounts'))
    return render(request, 'account/new_password.html')




def deleteUsers(request):
    if request.method != "POST":
        messages.error(request, "Access Denied")
    user = None
    id = request.POST.get('id')
    try:
        user = Acount_User.objects.get(id=id)
    except:
        messages.error(request, 'User not deleted')
    if user:
        try:
            user.delete()
            messages.success(request, 'User deleted successfully')
        except:
            messages.error(request, 'User not deleted')
    else:
        messages.error(request, 'User not deleted')
    
    return redirect(reverse('users'))





def viewUserById(request):
    id = request.GET.get('id', None)
    user = Acount_User.objects.filter(id=id)
    context = {}
    
    if not user.exists():
        context["code"] = 404
    else:
        context["code"] = 200
        user = user[0]
        context["id"] = user.id
        context["username"] = user.username
        context["first_name"] = user.first_name
        context["last_name"] = user.last_name
        context["phone"] = user.phone
        #print(context)
        
        return JsonResponse(context)
    
    
    








