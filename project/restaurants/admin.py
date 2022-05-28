from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Restaurant

# Apply summernote to all TextField in model.
class RestaurantAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('content',)


admin.site.register(Restaurant, RestaurantAdmin)