from django import forms
from models import Lower, Client, Appointment, TargetUser
from django.core import validators
from django.contrib.auth.models import User

class LowerForm(forms.ModelForm):
    class Meta:
        model = Lower
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['nom', 'pernom', 'telephone_protable', 'mail', 'password']

class ClientForm(forms.ModelForm):
    CIVI_CHOICES = [(0,"Mr"),(1,"Mme")] 
    civilite = forms.ChoiceField(choices=CIVI_CHOICES, widget=forms.RadioSelect())
    date_naissance = forms.DateField()
    class Meta:
        model = Client
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = [
            'civilite',
            'nom',
            'pernom',
            'telephone_fix',
            'telephone_protable',
            'adress',
            'pays',
            'ville',
            'code_postal',
            'date_naissance',
            'mail',
            'mail_invite',
            'password',
        ]

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['target_user', 'lawyer', 'date_rdv']

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(widget=forms.PasswordInput(),
                                label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(),
                                label="Password (again)")

    def clean_username(self): # check if username dos not exist before
        try:
            User.objects.get(username=self.cleaned_data['username']) #get user from user model
        except User.DoesNotExist :
            return self.cleaned_data['username']
        raise forms.ValidationError("this user exist already")


    def clean(self): # check if password 1 and password2 match each other
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:#check if both pass first validation
            if self.cleaned_data['password1'] != self.cleaned_data['password2']: # check if they match each other
                raise forms.ValidationError("passwords dont match each other")
        return self.cleaned_data


    def save(self): # create new user
        new_user=User.objects.create_user(username=self.cleaned_data['username'],
                                        password=self.cleaned_data['password1'],
                                        email=self.cleaned_data['email'],
                                            )
        new_user.first_name = self.cleaned_data['first_name']
        new_user.last_name = self.cleaned_data['last_name']
        new_user.is_active = False
        new_user.save()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']

class TargetUserForm(forms.ModelForm):
    CIVI_CHOICES = [(0,"Mr"),(1,"Mme")]
    civilite = forms.ChoiceField(choices=CIVI_CHOICES, widget=forms.RadioSelect())
    telephone_protable = forms.CharField()
    date_naissance = forms.DateField()
    adress = forms.CharField()
    code_postal = forms.CharField()
    mail_invite = forms.EmailField()
    class Meta:
        model = TargetUser
        fields = [
            'user',
            'civilite',
            'date_naissance',
            'telephone_protable',
            'adress',
            'code_postal',
            'mail_invite',
        ]

class AuthenticationForm(forms.Form):
    """
    Login form
    """
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        fields = ['username', 'password']