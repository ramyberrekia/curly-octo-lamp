from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Tour

# Apply summernote to all TextField in model.
class TourAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('content',)


admin.site.register(Tour, TourAdmin)