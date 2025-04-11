from .models import SiteSetting

def site_settings(request):
    setting = SiteSetting.objects.first()
    return {'site_setting': setting}