from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from .models import Listing

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3) # 3 listings per page 
    page = request.GET.get('page')

    paged_listings = paginator.get_page(page)

    context = {
        'listings' : paged_listings
    }

    return render(request, 'listings/listings.html', context)

def listing(request, id):
    return render(request, 'listings/listings.html', {})

def search(request):
    return render(request, 'listings/listings.html', {})

