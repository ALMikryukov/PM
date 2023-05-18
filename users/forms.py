from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Transaction

class CastomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username',  'email', 'password1', 'password2']
        labels = {
            'first_name': 'Name'

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
        