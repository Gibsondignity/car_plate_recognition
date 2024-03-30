from django.shortcuts import render, redirect, reverse
from .models import *
from account.models import *
from account.forms import *
from django.contrib import messages
import decimal

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import base64
from PIL import Image
import pytesseract

# Create your views here.
def profile(request):
    user = request.user
    security_question = SecurityAnswer.objects.filter(user=user).last()

    if security_question:
        security_form = SecurityQuestionForm(instance=security_question)
    else:
        security_form = SecurityQuestionForm()
        
    profile_form = ProfileForm(instance=request.user)
    
    
    if request.method == 'POST':
        if security_question:
            security_form = SecurityQuestionForm(request.POST or None, instance=security_question)
        else:
            security_form = SecurityQuestionForm(request.POST or None)
            
        profile_form = ProfileForm(request.POST or None, instance=request.user)
        
        if security_form.is_valid() and profile_form.is_valid():
            user = security_form.save(commit=False)
            user.user = request.user
            print(user.user)
            profile_form.save()
            user.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect(reverse('camera'))
        else:
            messages.error(request, security_form.errors.as_text())
            messages.error(request, profile_form.errors.as_text())
            print(profile_form.errors.as_text(), security_form.errors.as_text())
            
    context = {'security_form': security_form, 'profile_form': profile_form}
    return render(request, 'dashboard/profile.html', context)



def home(request):
    
    user = request.user
    reports = reportedCar.objects.filter(reported_by=user).all().order_by('-id')
    context = {'reports':reports}
    return render(request, 'dashboard/home.html', context)




def camera(request):
    
    
    if request.method == 'POST':
        # Get image data from POST request
        image_data = request.POST.get('image_data', '')

        # Extract image data from base64 string
        _, encoded_data = image_data.split(',', 1)
        decoded_data = base64.b64decode(encoded_data)

        # Save image to a temporary file
        with open('temp_image.png', 'wb') as f:
            f.write(decoded_data)

        # Perform OCR using pytesseract
        image = Image.open('temp_image.png')
        ocr_text = pytesseract.image_to_string(image)

        # Return OCR result as JSON response
        context = {}
        return render(request, 'dashboard/result.html', context)
    
    return render(request, 'dashboard/camera.html')




def chat(request):
    return render(request, 'dashboard/chat.html')




@csrf_exempt
def process_image(request):
    if request.method == 'POST':
        # Get image data from POST request
        image_data = request.POST.get('image_data', '')

        # Extract image data from base64 string
        _, encoded_data = image_data.split(',', 1)
        decoded_data = base64.b64decode(encoded_data)

        # Save image to a temporary file
        with open('temp_image.png', 'wb') as f:
            f.write(decoded_data)

        # Perform OCR using pytesseract
        image = Image.open('temp_image.png')
        ocr_text = pytesseract.image_to_string(image)

        # Return OCR result as JSON response
        return JsonResponse({'ocr_text': ocr_text})

    return JsonResponse({'error': 'Invalid request method'})