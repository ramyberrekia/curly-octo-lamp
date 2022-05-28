from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Hotel

# Apply summernote to all TextField in model.
class HotelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('content',)


admin.site.register(Hotel, HotelAdmin)