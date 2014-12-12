from django import forms
from models import Lower, Client

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