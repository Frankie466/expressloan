from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from .models import Customer
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, get_backends


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
            customer = form.save()  # This saves both User and Customer
            user = customer.user

            # Get the default authentication backend
            backend = get_backends()[0]  # Use the first backend
            user.backend = f'{backend.__module__}.{backend.__class__.__name__}'

            login(request, user)  # Log in the user
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'loan/register.html', {'form': form})
@login_required
def dashboard(request):
    customer = get_object_or_404(Customer, user=request.user)
    # Assign loan limit only when it's 0
    if customer.loan_limit == 0:
        customer.assign_loan_limit()
    processing_fee = customer.calculate_processing_fee()
    return render(request, 'loan/dashboard.html', {
        'customer': customer,
        'processing_fee': processing_fee,
        'till_number': '8600480'
    })



def home(request):
    return render(request, 'loan/home.html')

@login_required
def apply_loan(request):
    return render(request, 'loan/apply_loan.html')

@login_required
def loan_status(request):
    return render(request, 'loan/status.html')

@login_required
def repayment(request):
    return render(request, 'loan/repayment.html')

