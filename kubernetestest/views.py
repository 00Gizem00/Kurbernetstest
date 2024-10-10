from django.shortcuts import redirect, render

from kubernetestest.models import TestModel
from .forms import TestForm

def index(request):
    form = TestForm()
    if request.method == "POST":
        form = TestForm(request.POST)
        if form.is_valid():    
            form.save()
            return redirect("index")
    
    names = TestModel.objects.values_list("name", flat=True)
    
    
    return render(request, "index.html", {"form": form, "names": names})
    


