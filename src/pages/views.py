from django.shortcuts import render
from django.http import Http404
from .forms import ContactForm

# Create your views here.

# home_view()
def home_view(request):
    try:
        return render(request, 'home.html')
    except:
        raise Http404('Page does not exist')

# about_view()
def about_view(request):
    try:
        return render(request, 'about.html')
    except:
        raise Http404('Page does not exist')

# contact_view()
def contact_view(request):
    contact_form = ContactForm(request.GET)
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            print(contact_form.cleaned_data)
    context = {
        "contact_form": contact_form
    }
    print(contact_form)
    return render(request, 'contact.html', context)
