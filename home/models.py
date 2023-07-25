from django.db import models
from django.db.models.signals import post_save
from django_jalali.db import models as jmodels


class Invoice(models.Model):
    form_contract = models.CharField(max_length=300)
    company_name = models.CharField(max_length=300)
    address = models.CharField(max_length=300,null=True)
    name_of_the_company_manager = models.CharField(max_length=300)
    date_of_contract = models.DateField()
    contract_number = models.IntegerField()
    nationalid = models.CharField(max_length=300)
    telephone = models.CharField(max_length=300)
    mobile = models.CharField(max_length=300)
    contract_price = models.IntegerField()
    change = models.BooleanField(default=True)
    update = models.DateField(auto_now=True)
    date_of_cash_deposit = models.DateField()
    cash_deposit_amount = models.BigIntegerField()
    contract_type = models.CharField(max_length=300)
    overdue_account = models.IntegerField(null=True,blank=True)
    company_address = models.CharField(max_length=300)
    marketer = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    printing_cost = models.IntegerField()
    print_account_balance = models.IntegerField()
    print_the_deposited_amount = models.IntegerField()

    def save(self, *args, **kwargs): 
        self.overdue_account = int(self.contract_price) - int(self.cash_deposit_amount)
        super().save(*args, **kwargs)
    


class Product(models.Model):
    salary = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    phone_number = models.IntegerField()
    check_in_check_out = models.IntegerField()
    check_registration = models.IntegerField()
    due_date = models.DateField()
    change = models.BooleanField(default=True)
    update = models.DateField(auto_now=True)
    the_row_number = models.IntegerField()
    date_received = models.DateField()
    name_of_assignor = models.CharField(max_length=300)
    registered_check = models.IntegerField()
    bank_name = models.CharField(max_length=300)
    branch_name = models.CharField(max_length=300)
    check_number = models.IntegerField()
    check_amount = models.IntegerField()
    account_number =  models.IntegerField()
    due_date = models.DateField()
    pay_to = models.CharField(max_length=300)
    date = models.DateField()
    check_and_out = models.CharField(max_length=300)
    phone_number_of_the_owner_of_the_check = models.IntegerField()
    national_code = models.IntegerField()
    description = models.CharField(max_length=300)

    
   
    def __str__(self):
        return self.name

class Chart(models.Model):
    name = models.CharField(max_length=50, blank =True, null=True)
    company_name = models.CharField(max_length=300)
    overdue_account = models.IntegerField(null=True,blank=True)
    check_amount = models.IntegerField()
    update = models.DateTimeField(auto_now = True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True ,null=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE,  blank=True, null=True)

    
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        old_data = Chart.objects.filter(product__exact=self.product ,invoice__exact=self.invoice ,check_amount__exact=self.check_amount )
        if not old_data.exists():
            return super(Chart, self).save(*args, **kwargs)    




def product_post_saved(sender, instance, created, *args, **kwargs):
    data = instance
    if data.change == False:
        Chart.objects.create(product=data,check_amount=data.check_amount,update=data.update,company_name=data.name)

post_save.connect(product_post_saved, sender =Product)


def invoice_post_saved(sender, instance, created, *args, **kwargs):
    data = instance
    if data.change == False:
        Chart.objects.create(invoice=data,overdue_account=data.overdue_account,update=data.update,company_name=data.company_name)

post_save.connect(invoice_post_saved, sender =Invoice)