from django.db.models.fields import NullBooleanField
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView, CreateView, ListView
from .models import Customer, Transaction
from datetime import datetime
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
    
def CreateCustomer(request):
    if request.method=="POST":
        acc_no = request.POST.get('account_no')
        fname = request.POST.get('name')
        Email = request.POST.get('email')
        Balance = request.POST.get('balance')
        
        customer = Customer(
            account_no = acc_no,
            name = fname,
            email = Email,
            balance = Balance,
        )
        
        customer.save()
        
        messages.success(request, "Account was created for " + acc_no + ".")
        return redirect('home')
    context = {}
    return render(request, '../templates/createUser.html', context)
        
class ViewAllCustomers(ListView):
    template_name ='viewCustomer.html'
    model = Customer
    context_object_name = 'customer_list'
    
class TransferMoney(TemplateView):
    template_name = 'transferMoney.html'
    model = Customer

class TransferLogic(TemplateView):
    template_name = 'status.html'
    
    isVaild = None
    to = None
    fr = None
    a = None
    def dispatch(self, *args, **kwargs):
        self.to = self.request.GET['toAcc']
        self.fr = self.request.GET['fromAcc']
        self.a = int(self.request.GET['amount'])
        
        try:
            toAcc = Customer.objects.get(account_no = self.to)
            fromAcc = Customer.objects.get(account_no = self.fr)
            
            if(fromAcc.balance>=self.a):
                self.isValid = True
                fromAcc.balance -= self.a
                toAcc.balance += self.a
                
                Transaction.objects.create(to_account=toAcc.account_no,from_account=fromAcc.account_no,amount = self.a,transact_time=str(datetime.now()))
            else:
                self.isValid = False
                
            fromAcc.save()
            toAcc.save()
        except:
            self.isValid = False    

        return super().dispatch(*args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['valid'] = self.isValid
        
        return context
        
        
    
