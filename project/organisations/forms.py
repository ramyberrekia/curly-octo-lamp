from django import forms
from .models import Organisation


class OrganisationPostForm(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = ('name','description','address','image')


class ApproveOrDeclineOrgForm(forms.Form):
    CHOICES = (('A','Approved'),('D','Declined'))
    choice = forms.ChoiceField(choices=CHOICES)