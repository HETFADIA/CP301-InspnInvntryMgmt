from datetime import date
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .models import InvoiceModel
from users.models import Departments

# Create your views here.
@login_required(login_url='/accounts/login/')
def CreateRequest(request):
    
    if request.method == 'POST':

        vendor_name = request.POST.get('vendor_name')
        department = request.POST.get('department')
        date_of_delivery = request.POST.get('date_of_delivery')
        po_number = request.POST.get('po_number')
        po_date = request.POST.get('po_date')
        invoice_amount = request.POST.get('invoice_amount')
        invoice_number = request.POST.get('invoice_number')
        comments = request.POST.get('comments')

        invoice_amount = float(invoice_amount)
        print(vendor_name, date_of_delivery, po_number, department)

        if vendor_name == "" or date_of_delivery == "" or po_number == "" or department == "" :
            error = "All Fields Requirded"
            return render(request, 'home/error.html' , {'error':error})

        
        try : 

            myfile = request.FILES['invoice']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

            if myfile.size < 5000000 :

                    b = InvoiceModel(vendor_name=vendor_name, date_of_delivery=date_of_delivery, po_number=po_number, po_date=po_date, department = department, invoice_number = invoice_number, invoice_link = url, comments = comments, invoice_amount=invoice_amount, status = 0)
                    b.save()
                    return redirect('RequestPending')

            else:

                fs = FileSystemStorage()
                fs.delete(filename)

                error = "Your File Is Bigger Than 5 MB"
                return render(request, 'home/error.html' , {'error':error})

        except Exception as e:

            print(e)
            error = "Please provide the Invoice."
            return render(request, 'home/error.html' , {'error':error})
    
    dept = Departments.objects.all()
    return render(request, 'add_request/initiate_request.html', {'dept': dept})

def RequestPending(request):
    return render(request, 'add_request/list_request.html')