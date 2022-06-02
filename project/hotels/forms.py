from django import forms 
from .models import Hotel, HotelImage
from places.models import Place

class HotelCreateForm(forms.ModelForm):
    # pla = forms.(queryset)
    place = forms.ModelChoiceField(queryset=Place.objects.all())
    class Meta:
        model = Hotel
        fields = ('title','price','description','content','address', 'display_image')
        help_texts = {'description': 'A description for your room, It\'ll be shown in this hotel\'s card.'}