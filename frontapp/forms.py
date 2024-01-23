from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import AccountType
from .models import VenueOwner
from .models import Promoter
from .models import Concert
from .models import TicketOrder
from django.contrib.auth.decorators import login_required



class TicketOrderForm(forms.ModelForm):
    seat_type = forms.CharField(label='Seat Type', widget=forms.Select(choices=[('option1', 'Tier 1'), ('option2', 'Tier 2'), ('option3', 'Tier 3'), ('option4', 'Tier 4')]))
    class Meta:
        model = TicketOrder
        fields = ['seat_type', 'quantity']
        widgets = {
            'seat_type': forms.Select(attrs={'class': 'form-select'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control-sm'}),
        }
        

class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name':  forms.TextInput(attrs={'class': 'form-control'}),
            'username':   forms.TextInput(attrs={'class': 'form-control'}),
            'email':      forms.TextInput(attrs={'class': 'form-control-lg'}),
            'password1':  forms.TextInput(attrs={'class': 'form-control-lg'}),
            'password2':  forms.TextInput(attrs={'class': 'form-control-lg'}),
        }

class AccounTypeForm(forms.ModelForm):
    class Meta:
        model = AccountType
        fields = ['accType']

class VenueForm(forms.ModelForm):
    class Meta:
        model = VenueOwner
        fields = ['venueName', 'seats1', 'seats_capacity1', 'price1', 'seats2', 'seats_capacity2','price2', 'seats3', 'seats_capacity3','price3', 'seats4', 'seats_capacity4','price4']
        widgets = {
            'venueName':  forms.TextInput(attrs={'class': 'form-control'}),
            'seats1':     forms.TextInput(attrs={'class': 'form-control'}),
            'seats_capacity1':       forms.TextInput(attrs={'class': 'form-control-sm'}),
            'price1':     forms.TextInput(attrs={'class': 'form-control-sm'}),
            'seats2':     forms.TextInput(attrs={'class': 'form-control'}),
            'seats_capacity2':       forms.TextInput(attrs={'class': 'form-control-sm'}),
            'price2':     forms.TextInput(attrs={'class': 'form-control-sm'}),
            'seats3':     forms.TextInput(attrs={'class': 'form-control'}),
            'seats_capacity3':       forms.TextInput(attrs={'class': 'form-control-sm'}),
            'price3':     forms.TextInput(attrs={'class': 'form-control-sm'}),
            'seats4':     forms.TextInput(attrs={'class': 'form-control'}),
            'seats_capacity4':       forms.TextInput(attrs={'class': 'form-control-sm'}),
            'price4':     forms.TextInput(attrs={'class': 'form-control-sm'}),
        }


class ConcertForm(forms.ModelForm):
    class Meta:
        model = Concert
        fields = ['concertName', 'date', 'time']
        widgets = {
            'date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'time': forms.widgets.DateInput(attrs={'type': 'time'})
        }


#unfinished
class PromoterForm(forms.ModelForm):
    class Meta:
        model = Promoter
        fields = ['managed_concerts']
        widgets = {
            'managed_concerts':  forms.Select(attrs={'class': 'form-select form-select-sm'}),
        }
