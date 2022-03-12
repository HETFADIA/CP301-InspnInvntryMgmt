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
        widgets={
            'ir_number':forms.NumberInput(attrs={'class':'form-control'}),
            'ir_date': forms.TextInput(attrs={'class':'form-control'}),
            'department': forms.TextInput(attrs={'class':'form-control'}),
            'vendorName': forms.TextInput(attrs={'class':'form-control'}),
            'po_number': forms.TextInput(attrs={'class':'form-control'}),
            'po_date': forms.TextInput(attrs={'class':'form-control'}),
            'quantity': forms.NumberInput(attrs={'class':'form-control'}),
            'rate': forms.NumberInput(attrs={'class':'form-control'}),
            'amount': forms.NumberInput(attrs={'class':'form-control'}),
            'invoice_amount': forms.NumberInput(attrs={'class':'form-control'}),
            'invoice_number': forms.NumberInput(attrs={'class':'form-control'})
        }
    
