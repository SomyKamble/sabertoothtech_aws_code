from django import forms
from django.core import validators
import Sabertooth_Website_App

class UserDetails():
    def validateData(self,message,name):
        if len(message)==0:
            raise forms.ValidationError('Wait')

            
        
        