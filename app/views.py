from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.core.urlresolvers import reverse
from models import Lower, Client
from forms import LowerForm

#django defaut listView
class LowerIndexView(generic.ListView):
    model = Lower
    template_name = "lower_index.html"
    context_object_name = "lower_list"

def lowerDetailView(request, lower_id):
    lower = get_object_or_404(Lower, pk=lower_id)
    return render(request, 'lower_detail.html', {'lower': lower})

#create and update the lower
def CreateLowerView(request):
    if request.method == 'POST':
        data = request.POST
        print data
        form = LowerForm(data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('lower')
        else: 
            return render(request, 'lower_create.html', {'form': form})
    else:
        form = LowerForm()
        return render(request, 'lower_create.html', {'form': form})

class ClientIndexView(generic.ListView):
    model = Client
    template_name = "client_index.html"
    context_object_name = "client_list"

def clientDetailView(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    return render(request, 'client_detail.html', {'client': client})
