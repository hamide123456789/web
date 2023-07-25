from django.shortcuts import render,redirect ,get_object_or_404
from .forms import InvoiceForm ,ProductForm
from .models import Invoice , Product , Chart
import datetime
from django.views import View






def invoice_list(request):
    invoices = Invoice.objects.all()
    form = InvoiceForm()
    context = {
        'invoices': invoices,
        'form': form,
    }
    return render(request, 'home.html', context)
  

def invoice_detail(request, pk):
    invoice = get_object_or_404(Invoice, id=pk)
    form = InvoiceForm()
    context = {
        'invoice': invoice,
        'form': form,
    }

    return render(request, 'detail.html', context)

# class invoice_detail(View):
#     def setup(self, request, *args, **kwargs):
#         self.product = get_object_or_404(Invoice, id=kwargs['pk'])
#         self.change = Chart.objects.filter(invoice_id=kwargs['pk'])
       
        
#         return super().setup(request,*args,**kwargs)


    
#     def get(self, request, *args, **kwargs):
#         # invoice = get_object_or_404(Product, id = self.kwargs["pk"])
#         obj = Invoice.objects.get(id = self.kwargs["pk"])
#         form = InvoiceForm()
#         # date = obj.values_list("update ", flat=True)
#         # price = obj.values_list("overdue_account", flat=True)
#         context = {
#         'obj': obj,
#         'form': form,
#         'date':obj.update,
#         'price':obj.overdue_account,
#         }
#         print (context)
#         return render(request, 'detail.html', context)


def save_chart(request):
    products = Invoice.objects.values('product').distinct()
    for product in products:
        prices = Invoice.objects.filter(product=product['product']).values_list('check_amount', flat=True)
        dates = Invoice.objects.filter(product=product['product']).values_list('date', flat=True)

        
        chart = Chart(product=product['product'],
                      prices=','.join(str(price) for price in prices),
                      dates=','.join(str(date) for date in dates))
        chart.save()

    return render(request, 'chart_saved.html')
    




def create_view(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = InvoiceForm()
    return render(request, 'create.html', {'form': form})

    

    
def invoice_update_view(request, pk):
    invoice_obj = get_object_or_404(Invoice, pk=pk)
    form = InvoiceForm(request.POST or None, instance=invoice_obj)
    context = {
        'form': form,
    }

    if form.is_valid():
        form.save()
        return redirect('home:home')

    return render(request, 'invoice_update_view.html', context)

   

def delete_view(request, pk):
    item = get_object_or_404(Invoice, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('home:home')
    return render(request, 'delete.html', {'item': item})


def my_view(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    events = None
    if start_date and end_date:
        events = Invoice.objects.filter(date_of_contract__range=(start_date, end_date))

    return render(request, 'my_view.html', {'events': events})


# def index(request):
#     products = Product.objects.all()
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('home:index')
#     else:
#         form = ProductForm()

#     context = {
#         'products': products,
#         'form': form,
#     }
#     return render(request,'index.html',context)





def product_list(request):
    products = Product.objects.all()
    form = ProductForm()
    context = {
        'products': products,
        'form': form,
    }
    return render(request, 'product.html', context)
  

# def product_detail(request, pk):
#     product = get_object_or_404(Product, id=pk)
#     form = ProductForm()

#     context = {
#         'product': product,
#         'form': form,
#     }

#     return render(request, 'product_detail.html', context)




class product_detail(View):
    def setup(self, request, *args, **kwargs):
        self.product = get_object_or_404(Product, id=kwargs['pk'])
        self.change = Chart.objects.filter(product_id=kwargs['pk'])
       
        
        return super().setup(request,*args,**kwargs)


    # def product_detail(request, pk):
    def get(self, request, *args, **kwargs):
        obj = Product.objects.get(id = self.kwargs["pk"])
        form = ProductForm()
        context = {
        'obj': obj,
        'form': form,
        'date':obj.update,
        'price':obj.check_amount,
        }
        return render(request, 'product_detail.html', context)



        


def product_create_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:product')
    else:
        form = ProductForm()
    return render(request, 'product_create.html', {'form': form})

    

    
def product_update_view(request, pk):
    product_obj = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product_obj)
    context = {
        'form': form,
    }

    if form.is_valid():
        form.save()
        return redirect('home:producte')

    return render(request, 'product_update_view.html', context)

   

def product_delete_view(request, pk):
    item = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('home:product')
    return render(request, 'delete.html', {'item': item})


def product_my_view(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    events = None
    if start_date and end_date:
        events = Invoice.objects.filter(date_of_contract__range=(start_date, end_date))

    return render(request, 'product_my_view.html', {'events': events})








