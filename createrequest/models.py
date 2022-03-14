from django.db import models

# Create your models here.

class InvoiceModel(models.Model):

    vendor_name      = models.CharField(max_length = 200)
    department       = models.CharField(max_length = 200)
    date_of_delivery = models.DateField()
    po_number        = models.CharField(max_length = 200)
    po_date          = models.CharField(max_length = 200)
    invoice_amount   = models.FloatField(default=0)
    invoice_number   = models.TextField(default='')
    invoice_link     = models.TextField(default='')
    last_update      = models.DateTimeField(auto_now_add=True)
    comments = models.TextField(default='')
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.vendor_name