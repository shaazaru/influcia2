from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model,login
from django.contrib import auth
from django.contrib.auth.models import auth
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import FormView,TemplateView
from django.contrib.auth.forms import authenticate
from django.contrib import messages
from .forms import Brandregister
from .models import MyUserManager, User


class BrandRegistration(FormView):
    form_class = Brandregister
    template_name = 'BrandRegister.html'
    msg_flag = False

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            submit = request.POST.get("submit")
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save(commit=True)
                messages.info( request, "Registration successfuly completed.")
                return render(request,'brandlogin.html')
            else:
                email = form.data.get("email")
                Business_Name = form.data.get('Business_Name')
                Business_Website = form.data.get('Business_Website')
                First_Name = form.data.get('First_Name')
                Last_Name = form.data.get('Last_Name')
                Phone_Number = form.data.get('Phone_Number')

                ctx = {'form': form, 'submit':submit, 'email':email, 'Business_Name': Business_Name,
                        'Business_Website': Business_Website,'First_Name': First_Name, 
                        'Last_Name' : Last_Name, 'Phone_Number':Phone_Number,}
                return render(request, self.template_name, ctx)
            form = self.form_class()
            outctx = {'form': form, 'submit':submit,}
        return render(request, self.template_name, outctx)

def brandlogin_view(request):

     # here you get the post request username and password
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    # authentication of the user, to check if it's active or None
    user = auth.authenticate(username=username, password=password)

    if user and user.is_authenticated:
        return render(request, 'branddashboard.html')

    else:
        return HttpResponseRedirect("Invalid username or password")


class BrandHomeView(TemplateView):
    template_name = "brandhome.html"

class BrandDashboardView(TemplateView):
    template_name = "branddashboard.html"