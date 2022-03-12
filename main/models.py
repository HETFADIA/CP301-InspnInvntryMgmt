from django.db import models

# Create your models here.

class InvoiceModel(models.Model):
    # drr_number = models.IntegerField(default=0)
    # drr_date = models.CharField(max_length = 200)
    ir_number      = models.IntegerField(default=0)
    ir_date        = models.CharField(max_length = 200)
    department     = models.CharField(max_length = 200)
    vendorName     = models.CharField(max_length = 200)
    po_number      = models.CharField(max_length = 200)
    po_date        = models.CharField(max_length = 200)
    quantity       = models.IntegerField(default=1)
    rate           = models.IntegerField(default=0)
    amount         = models.IntegerField(default=0)
    invoice_amount = models.IntegerField(default=0)
    invoice_number = models.IntegerField(default=0)

    def __str__(self):
        return self.vendorName


    
