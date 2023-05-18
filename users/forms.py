from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Transaction
from django import forms

class CastomUserCreationForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input',
                                                             'placeholder': 'имя пользователя'}))
    
    first_name  = forms.CharField(widget=forms.TextInput(attrs={'class': 'input',
                                                             'placeholder': 'имя'})) 
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input',
                                                            'placeholder': 'email'}))  
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input',
                                                      'placeholder':'введите пароль'}))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input',
                                                      'placeholder':'повторите пароль'}))



    class Meta:
        model = User
        fields = [ 'username' , 'first_name' , 'email', 'password1', 'password2' , ]
        labels = {
            # 'first_name': 'Name'

        }

    def __init__(self, *agrs ,**kwargs):
        super(CastomUserCreationForm, self).__init__(*agrs, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name' , 'profile_image' , 'phoneNumber']
 
    def __init__(self, *agrs ,**kwargs):
        super(ProfileForm, self).__init__(*agrs, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class TransactionForm(ModelForm):

    class Meta:
        model = Transaction
        fields = ['title', 'amount', 'is_deposit']
        