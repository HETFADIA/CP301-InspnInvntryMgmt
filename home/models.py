from django.db import models

# Create your models here.

class InvoiceModel(models.Model):

    ir_number        = models.IntegerField(default=0)
    ir_date          = models.DateField()
    department       = models.CharField(max_length = 200)
    vendor_name      = models.CharField(max_length = 200)
    po_number        = models.CharField(max_length = 200)
    po_date          = models.CharField(max_length = 200)
    invoice_amount   = models.FloatField(default=0)
    invoice_number   = models.TextField(default='')
    invoice_link     = models.TextField(default='')
    date_of_delivery = models.DateField()
    last_update      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vendor_name