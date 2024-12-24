from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile,Address
from django import forms
from django.forms.widgets import PasswordInput,TextInput
class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
   
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())

class Profileform(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['fname','mobile']
'''class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['name', 'a_mobile', 'pincode', 'house_no', 'area', 'landmark','city','state']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),  # Use TextInput
            'a_mobile': forms.NumberInput(attrs={'placeholder': 'Phone number'}),  # Use NumberInput
            'pincode': forms.TextInput(attrs={'placeholder': 'Pincode'}),  # Use TextInput
            'house_no': forms.TextInput(attrs={'placeholder': 'House No. or Building Name'}),  # Use TextInput
            'area': forms.TextInput(attrs={'placeholder': 'Road name, Area, Colony'}),  # Use TextInput
            'landmark': forms.TextInput(attrs={'placeholder': 'Landmark'}),  
            'city': forms.TextInput(attrs={'readonly': 'readonly', 'placeholder': 'City'}),  # Readonly
            'state': forms.TextInput(attrs={'readonly': 'readonly', 'placeholder': 'State'})  # Readonly
        }'''
