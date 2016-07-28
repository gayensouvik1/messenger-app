from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login

from django.core.urlresolvers import reverse

from .models import Document
from .forms import DocumentForm
 



@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create(
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )

            u = User.objects.get(username=form.cleaned_data['username'])
            u.set_password(form.cleaned_data['password1'])
            u.save()

            
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )


def register_success(request):
    return render_to_response(
    'registration/success.html',
    )

def home(request):
    return render(request,"home.html",{})





def logout_success(request):
    logout(request)
    return render_to_response(
    'registration/logout_success.html',
    )
    


def contact(request):
    return render(request,"contact.html",{})


def profile(request):
    
    if request.method == 'POST' and request.POST['toUser'] is not '':
        Message.objects.create(receiver=request.POST['toUser'], sender=request.user, message=request.POST['message'] )

    context = {'list': Message.objects.all(), 'me' : request.user }
    return render(request,"profile.html",context)

def list(request):
    
    if request.method == 'POST':
    
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
            

            return HttpResponseRedirect(reverse('messenger.views.list'))
    else:
        form = DocumentForm() 
            
    return render_to_response(
        'list.html',
        { 'form': form},
        context_instance=RequestContext(request)
    )


def list_only(request):
    documents = Document.objects.all()
    return render(request,'list_only.html',{'documents':documents})