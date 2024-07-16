from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateCustomerForm, UpdateCustomerForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Customer
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required

# Home page
def home(request):
  return render(request, 'myapp/index.html')


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            User.objects.create_user(username=username, password=password)
            return redirect('login')  
        else:
           print("Form is not valid")
    return render(request, 'myapp/register.html', {'form': form})

#login user

def my_login(request):

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password')
           user = authenticate(request, username=username, password=password)
           if user is not None:
              login(request, user)
              return redirect("index")
           else:
              error_message = "Invalid username or password. Please try again."
              context = {'error_message': error_message}
              return render(request, 'myapp/login.html', context=context)
    context = {'form':form}
    return render(request, 'myapp/login.html', context=context)

#Dashboard
@login_required(login_url='login')
def dashboard(request):
   customers = Customer.objects.all()
   context = {'customers': customers}
   return render(request, 'myapp/index.html', context=context)

@login_required(login_url='login')
def create_customer(request):

    form = CreateCustomerForm()

    if request.method == "POST":

        form = CreateCustomerForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your Customer was created!")

            return redirect("index")

    context = {'form': form}

    return render(request, 'myapp/create-customer.html', context=context)


# - Update a Customer 

@login_required(login_url='login')
def update_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    print(customer)
    if request.method == 'POST':
        form = UpdateCustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Your customer was updated!")
            return redirect("index")
        
    context = {'customer': customer}
    return render(request, 'myapp/update-customer.html', context=context)

# - Read / View a singular Customer

@login_required(login_url='login')
def singular_customer(request, pk):

    all_customers = Customer.objects.get(id=pk)

    context = {'customer':all_customers}

    return render(request, 'myapp/view-customer.html', context=context)


# - Delete a Customer

@login_required(login_url='login')
def delete_customer(request, pk):

    record = Customer.objects.get(id=pk)

    record.delete()

    messages.success(request, "Your Customer was deleted!")

    return redirect("index")



# - User logout

def user_logout(request):

    auth.logout(request)

    messages.success(request, "Logout success!")

    return redirect("my-login")
