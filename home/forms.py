from .models import Invoice, Product
from django import forms




class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        # exclude = ['date_of_contract', ]
        fields = "__all__" 





class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__" 
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'check_amount': forms.TextInput(attrs={'class': 'form-control'}),

        }