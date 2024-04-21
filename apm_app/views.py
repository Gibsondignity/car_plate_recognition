import json
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
import io

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


def recentReportedCars(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        car_number = request.POST.get('car_number')
        
        issue = reportedCar(car_number, reported_issue=comment, reported_by=request.user)
        issue.save()
        
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

        try:
            # Extract image data from base64 string
            _, encoded_data = image_data.split(',', 1)
            decoded_data = base64.b64decode(encoded_data)

            # Validate and open the image using Pillow
            image = Image.open(io.BytesIO(decoded_data))
            
            # Perform OCR using pytesseract
            ocr_text = pytesseract.image_to_string(image)

            # Assuming carinfo is an instance of your model
            carinfo = CarInfo.objects.filter(car_number=ocr_text).first()

            context = {
                'car_number': carinfo.car_number,
                'car_owner': carinfo.owner_name,
                'picture': carinfo.picture.url if carinfo.picture else None,
                'owner_dob': carinfo.owner_dob,
                'car_model': carinfo.car_model,
                'car_type': carinfo.car_type,
                'color': carinfo.color,
                'date_of_reg': carinfo.date_of_reg,
                'region_of_reg': carinfo.region_of_reg,
                'owner_phone': carinfo.owner_phone,
            }

            return JsonResponse(context, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        
    return JsonResponse(status=405)




def searchCarNumber(request):
    if request.method == "POST":
        carnumber = json.loads(request.body)
        print(carnumber['carnumber'])
        carinfo = CarInfo.objects.filter(car_number=carnumber['carnumber']).first()
        
        context = {
            'car_number': carinfo.car_number,
            'car_owner': carinfo.owner_name,
            'picture': carinfo.picture.url if carinfo.picture else None,
            'owner_dob': carinfo.owner_dob,
            'car_model': carinfo.car_model,
            'car_type': carinfo.car_type,
            'color': carinfo.color,
            'date_of_reg': carinfo.date_of_reg,
            'region_of_reg': carinfo.region_of_reg,
            'owner_phone': carinfo.owner_phone,
        }
    
        print(list(context.values()))
    return  JsonResponse(context, status=200, safe=False)



def reportIssue(request):
    reportedCar