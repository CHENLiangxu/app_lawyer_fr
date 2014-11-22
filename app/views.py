from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views import generic
from django.core.urlresolvers import reverse
from models import Lower, Client

#django defaut listView
class LowerIndexView(generic.ListView):
    model = Lower
    template_name = "lower_index.html"
    context_object_name = "lower_list"

def LowerDetailView(request, lower_id):
    lower = get_object_or_404(Lower, pk=lower_id)
    return render(request, 'lower_detail.html', {'lower': lower})

class ClientIndexView(generic.ListView):
    model = Client
    template_name = "client_index.html"
    context_object_name = "client_list"

def ClientDetailView(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    return render(request, 'client_detail.html', {'client': client})
