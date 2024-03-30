from django.contrib.auth.models import Group
from django import forms
from .models import *
              
        
class RegisterForm(forms.ModelForm):
    class Meta:
        model = Acount_User
        fields = ('username', 'password')
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'required': True}), 
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'required': True}),
        }
        
        
class SecurityQuestionForm(forms.ModelForm):
    class Meta:
        model = SecurityAnswer
        fields = ('question', 'answer_text')
        
        widgets = {
            'question': forms.Select(attrs={'class': 'form-control', 'required': True}), 
            'answer_text': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }
        


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Acount_User
        fields = ('first_name', 'second_name', 'phone',)
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control',}), # 'placeholder': 'First Name
            'second_name': forms.TextInput(attrs={'class': 'form-control', }), 
            'phone': forms.TextInput(attrs={'class': 'form-control', }),
        }
        



# class SecurityAnswerForm(forms.Form):
#     answer = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
#     question = forms.Select()