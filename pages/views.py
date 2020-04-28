from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from realtors.models import Realtor

from listings.choices import bedrooms, state_choices, price_choices

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    
    context = {
        'listings' : listings,
        'state_choices' : state_choices,
        'bedrooms' : bedrooms,
        'price_choices' : price_choices,
    }
    
    return render(request, 'pages/index.html', context)

def about(request):
    realtors = Realtor.objects.all()

    context = {
        'realtors' : realtors,
    }

    return render(request, 'pages/about.html', context) 