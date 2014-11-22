from django import forms
from models import Lower
class LowerForm(forms.ModelForm):
    class Meta:
        model = Lower
        fields = ['nom', 'pernom', 'telephone_protable', 'mail', 'password']