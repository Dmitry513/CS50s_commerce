from django import forms
from .models import Commodity


class CommodityForm(forms.ModelForm):
    class Meta:
        model = Commodity
        fields = ('name', 'description', 'image', 'startprice')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'startprice': forms.TextInput(attrs={'class': 'form-control'}),
        }
