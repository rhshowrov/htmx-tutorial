from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Contact
from django.db.models import Q
# Create your views here.
@login_required
def index(request):
    contacts=request.user.contacts.all().order_by('-created_at')
    context={'contacts':contacts}
    return render(request,'contacts/contacts.html',context=context)


def search_contacts(request):
    serach_text=request.GET.get('search','')
    contacts=request.user.contacts.filter(Q(name__icontains=serach_text) | Q(email__icontains=serach_text))
    return render(request,'contacts/partials/contacts-list.html',context={
        'contacts':contacts,
    })