from django import forms
from django.contrib.auth.models import User
from .models import Customer


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class RegisterForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    id_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    next_of_kin_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    next_of_kin_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    employment_status = forms.ChoiceField(
        choices=Customer.employment_status.field.choices,   # ✅ Fixed here
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Customer
        fields = ['full_name', 'dob', 'id_number', 'phone_number', 'next_of_kin_name', 'next_of_kin_phone', 'employment_status']

    def save(self, commit=True):
        # Create the User first
        user = User.objects.create_user(
            username=self.cleaned_data['email'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        # Assign user to the customer
        customer = super().save(commit=False)
        customer.user = user
        if commit:
            customer.save()
        return customer
