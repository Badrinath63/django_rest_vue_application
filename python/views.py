from django.shortcuts import render
from administrator.forms import Contactform, Adminregisterform
from administrator.models import Adminregistermodel, Contactmodel
from vendors.models import Vendorregistermodel, Productmodel
from customers.models import Customerregistermodel, Feedbackmodel
// hai i am pavan
# Create your views here.
def about(request):
    return render(request, "about.html", {})

def bloghome(request):
    return render(request, "blog-home.html", {})

def blogsingle(request):
    return render(request, "blog-single.html", {})

def contact(request):
    form=Contactform()
    if request.method=='POST':
        details=Contactform(request.POST)
        if details.is_valid():
            details.save()
            return render(request, "contact.html", {'form': form, 'msg':'Thanks for Contacting Us'})
    return render(request, "contact.html", {'form':form})

def departments(request):
    return render(request, "departments.html", {})

def doctors(request):
    return render(request, "doctors.html", {})

def elements(request):
    return render(request, "elements.html", {})

def features(request):
    return render(request, "features.html", {})

def index(request):
    return render(request, "index.html", {})

def administratorindex(request):
    email = request.session['email']
    view = Adminregistermodel.objects.get(email=email)
    return render(request, 'administrator_index.html', {'view': view.name})

def adminlogin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        login=Adminregistermodel.objects.filter(email=email, password=password)
        elogin=Adminregistermodel.objects.filter(email=email)
        view = Adminregistermodel.objects.get(email=email)
        if len(login)==1:
            request.session["email"] = email
            return render(request, "administrator_index.html", {'view': view.name, 'msg':'Login Successful'})
        elif len(elogin)==0:
            return render(request, "administrator_register.html", {'msg':'Email Not Registered'})
        else:
            return render(request, "administrator_login.html", {'msg':'Invalid Credentials'})
    return render(request, "administrator_login.html", {})

def adminregister(request):
    if request.method=='POST':
        details=Adminregisterform(request.POST)
        email=request.POST['email']
        count=Adminregistermodel.objects.filter(email=email)
        if len(count)==0:
            if details.is_valid():
                details.save()
                return render(request, "administrator_index.html", {'msg':'Registration successful'})
            else:
                return render(request, "administrator_index.html", {'msg': 'Email already registered'})
    return render(request, "administrator_register.html", {})

def adminlogout(request):
    request.session["email"]=""
    return render(request, 'administrator_login.html', {'msg': 'logout successful'})

def adminchangepassword(request):
    if request.method == 'POST':
        email = request.session['email']
        oldpassword = request.POST['oldpassword']
        newpassword = request.POST['newpassword']
        count = Adminregistermodel.objects.filter(email=email, password=oldpassword)
        if len(count)==1:
            count = Adminregistermodel.objects.get(email=email, password=oldpassword)
            count.password = newpassword
            count.save()
            return render(request, "administrator_index.html", {'msg': 'Password Change successful'})
        else:
            return render(request, 'administrator_changepassword.html', {'msg': 'invalid oldpassword'})
    return render(request, 'administrator_changepassword.html', {})

def viewvendors(request):
    view=Vendorregistermodel.objects.all
    return render(request, 'viewvendors.html', {'view':view })

def viewcustomers(request):
    view=Customerregistermodel.objects.all
    return render(request, 'viewcustomers.html', {'view':view})

def viewfeedback_admin(request,vemail):
    view=Feedbackmodel.objects.filter(vemail=vemail)
    return render(request, 'viewfeedback_admin.html', {'view':view})

def viewcontacted(request):
    view=Contactmodel.objects.all
    return render(request, 'view_contactus.html', {'view':view})

def customer_delete(request,id):
    cus=Customerregistermodel.objects.get(id=id)
    cus.delete()
    view=Customerregistermodel.objects.all()
    return render(request, 'viewcustomers.html', {'view': view, 'msg':'Deleted'})

def vendor_delete(request,id):
    cus=Vendorregistermodel.objects.get(id=id)
    cus.delete()
    view=Vendorregistermodel.objects.all()
    return render(request, 'viewvendors.html', {'view': view, 'msg':'Deleted'})

def view_products(request):
    view=Productmodel.objects.all()
    return render(request, 'viewproducts_admin.html', {'view': view})