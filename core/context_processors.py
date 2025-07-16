from .models import SocialLink
import requests

def social_links(request):
    return {'social_links': SocialLink.objects.all()}

# Add currency rates to context
API_KEY = '8d65df6517-4ad2ea7b3f-szh76b'
API_URL = 'https://api.primeapi.io/fx/quote?pairs=NPR/USD,NPR/EUR'

def currency_rates(request):
    rates = {'NPR': 1, 'USD': 0.0075, 'EUR': 0.0069}  # fallback
    try:
        res = requests.get(API_URL, headers={'X-API-Key': API_KEY}, timeout=5)
        data = res.json().get('data', {})
        if 'NPR/USD' in data:
            rates['USD'] = data['NPR/USD']['mid']
        if 'NPR/EUR' in data:
            rates['EUR'] = data['NPR/EUR']['mid']
    except Exception:
        pass
    return {'currency_rates': rates} 