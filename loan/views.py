from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from .models import Customer




def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid email or password')
    else:
        form = LoginForm()
    return render(request, 'loan/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            user = form.save_user()  # ✅ Fixed the issue here
            customer.user = user
            customer.assign_loan_limit()  # ✅ Assign loan limit to the customer
            customer.save()
            login(request, user)  # ✅ Automatically login the user
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'loan/register.html', {'form': form})


def dashboard(request):
    customer = Customer.objects.get(user=request.user)

    # Assign loan limit only when it's 0
    if customer.loan_limit == 0:
        customer.assign_loan_limit()

    processing_fee = customer.calculate_processing_fee()
    return render(request, 'loan/dashboard.html', {
        'customer': customer,
        'processing_fee': processing_fee,
        'till_number': '0712345678'
    })



def home(request):
    return render(request, 'loan/home.html')


def apply_loan(request):
    return render(request, 'loan/apply_loan.html')


def loan_status(request):
    return render(request, 'loan/status.html')


def repayment(request):
    return render(request, 'loan/repayment.html')

