from django import forms
from .models import InvoiceModel

class InvoiceModelForm(forms.ModelForm):
    class Meta:
        model = InvoiceModel
        fields = [
            'ir_number',   
            'ir_date',     
            'department',    
            'vendorName',     
            'po_number',      
            'po_date',       
            'quantity',       
            'rate',          
            'amount',         
            'invoice_amount',
            'invoice_number',
        ]
    
