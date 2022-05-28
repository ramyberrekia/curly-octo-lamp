from .models import siteSettings

def settings(request):
    site_settings = siteSettings.objects.first()

    return {'settings':site_settings}