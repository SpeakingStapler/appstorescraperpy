from .core import AppleScraper
from .models import App


def get_app(app_id,country='us') -> App:
    _details = AppleScraper._get_app_details(app_id,country)

    return App(_details,country)
