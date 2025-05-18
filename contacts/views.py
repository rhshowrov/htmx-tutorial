from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Contact
from django.db.models import Q
from .forms import ContactForm
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
@login_required
def index(request):
    contacts=request.user.contacts.all().order_by('-created_at')
    form=ContactForm()
    context={'contacts':contacts,'form':form}
    return render(request,'contacts/contacts.html',context=context)

@login_required
def search_contacts(request):
    import time
    time.sleep(2)
    serach_text=request.GET.get('search','')
    contacts=request.user.contacts.filter(Q(name__icontains=serach_text) | Q(email__icontains=serach_text))
    return render(request,'contacts/partials/contacts-list.html',context={
        'contacts':contacts,
    })

@require_http_methods(['POST'])
@login_required
def create_contact(request):
    form=ContactForm(request.POST,request.FILES, initial={'user':request.user})
    if form.is_valid():
        contact=form.save(commit=False)
        contact.user=request.user
        contact.save()
        context={'contact':contact}
        response= render(request,'contacts/partials/contact-row.html',context=context)
        response['HX-Trigger']='contact-success'
        return response
    else:
        response=render(request,'contacts/partials/add-contact-modal.html',context={'form':form})
        response['HX-retarget']='#contact_modal'
        response['HX-Reswap']='outerHTML'
        response['HX-Trigger-After-Settle'] = 'fail'
        return response
    
@require_http_methods(['DELETE'])
@login_required
def delete_contact(request,pk):
    contact=get_object_or_404(Contact,pk=pk,user=request.user)
    contact.delete()
    response=HttpResponse(status=204)
    response['HX-Trigger']='contact-deleted'
    return response

