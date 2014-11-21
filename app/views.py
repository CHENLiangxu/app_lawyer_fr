from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views import generic
from django.core.urlresolvers import reverse
from models import Lower

class LowerIndexView(generic.ListView):
    model = Lower
    template_name = "lower_index.html"
    context_object_name = "lower_list"

def LowerDetailView(request, lower_id):
    lower = get_object_or_404(Lower, pk=lower_id)
    return render(request, 'lower_detail.html', {'lower': lower})
