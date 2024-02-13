from django.shortcuts import render,redirect

from .models import contact_forms_models
from .forms import contactforms
# Create your views here.






def contact(request):
    allcontact = contact_forms_models.objects.all()
    if request.method == 'POST':
       form = contactforms(request.POST)
       if form.is_valid():
           form.save()
           return redirect('contact_name')
    else:
        form = contactforms()

    context = {

        'title': 'contact page',
        'all': allcontact, 
        'form': form

    }

    return render(request, 'contact.html', context=context)
