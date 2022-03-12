from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse

from .forms import InvoiceModelForm



@login_required(login_url='login/')
def fill_Invoice(request):
    if request.user.is_authenticated:
        form = InvoiceModelForm()

        if request.method == 'POST':
            print("aa rha h....aaaa rhaa h...data aa rha h....🤩")

        context = {'form': form}
        return render(request, 'main/newinvoice.html', context)
    else:
        # TODO: message to be changed
        return HttpResponse("kaha ghuse chle aa rhe ho bhsdk!!..login kro pehle beta!")
    