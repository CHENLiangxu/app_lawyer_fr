from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render, render_to_response, RequestContext, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.core.urlresolvers import reverse
from models import Lower, TargetUser, Appointment
from forms import LowerForm, TargetUserForm, AuthenticationForm, UserForm, AppointmentForm
from django.utils.translation import ugettext, activate, get_language

from datetime import datetime

#django defaut listView
def my_view(request):
    if request.user.is_authenticated():
        output = ugettext("welcome back")
        old_lang = get_language()
        output = repr(old_lang) + output
        output += str(request.user.id)
    else:
        output = ugettext("welcome")
        old_lang = get_language()
        output = repr(old_lang) + output
    
    return HttpResponse(output)

class LowerIndexView(generic.ListView):
    model = Lower
    template_name = "lower_index.html"
    context_object_name = "lower_list"

def lowerDetailView(request, lower_id):
    lower = get_object_or_404(Lower, pk=lower_id)
    return render(request, 'lower_detail.html', {'lower': lower})

#create the lower
def CreateLowerView(request):
    if request.method == 'POST':
        data = request.POST
        form = LowerForm(data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('lower')
        else: 
            return render(request, 'lower_create.html', {'form': form})
    else:
        form = LowerForm()
        return render(request, 'lower_create.html', {'form': form})

class AppointmentIndexView(generic.ListView):
    model = Appointment
    template_name = "appointment_index.html"
    context_object_name = "appointment_list"

def AppointmentDetailView(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    return render(request, 'appointment_detail.html', {'appointment': appointment})

#create the appointment
def CreateAppointmentView(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            data = request.POST
            form = AppointmentForm(data)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('appointment')
            else:
                return render(request, 'appointment_create.html', {'form':form})
        else:
            form = AppointmentForm()
            target = TargetUser.objects.get(user_id=request.user.id)
            content = {
                "form" : form,
                "target": target,
                "now" : datetime.now().replace(microsecond=0).strftime("%Y-%m-%d %H:%M:%S")
            }
            return render(request, 'appointment_create.html', content)
    else:
        return redirect('login')

class TargetUserIndexViews(generic.ListView):
    model = TargetUser
    template_name = "target_user_index.html"
    context_object_name = "target_user_list"

def TargetUserDetailView(request, target_user_id):
    target = get_object_or_404(TargetUser, pk=target_user_id)
    user = User.objects.get(id=target.user_id)
    content = {
        "target": target,
        "user": user,
    }
    return render(request, 'target_user_detail.html', content)

def CreateUserView(request):
    if request.method == 'POST':
        data = request.POST
        form = UserForm(data)
        if form.is_valid():
            form.clean_username()
            form.clean()
            form.save()
            return HttpResponseRedirect('login')
        else:
            return render(request, 'user_create.html', {'form': form})
    else:
        form = UserForm()
        return render(request, 'user_create.html', {'form': form})

"""
if not login, can not create a target
if login at first time, need to create target at once
"""
def CreateTargetUserView(request):
    content = {}
    user = request.user
    content['user'] = user
    if request.method == 'POST':
        data = request.POST
        form = TargetUserForm(data)
        content['form'] = form
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('target_user')
        else:
            return render(request, 'target_user_create.html', content)
    else:
        form = TargetUserForm()
        content['form'] = form
        return render(request, 'target_user_create.html', content)

        

def LoginView(request):
    """
    Log in view
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        content = {}
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('test')
                else:
                    content = {}
                    form = TargetUserForm()
                    content['form'] = form
                    content['user'] = user
                    return render(request, 'target_user_create.html', content)
            else:
                content['info'] = "can not login in"
                return render(request, 'login.html', content)
    else:
        form = AuthenticationForm()
    return render_to_response('login.html', {
        'form': form,
    }, context_instance=RequestContext(request))

def LogoutView(request):
    logout(request)
    return redirect('/')


